"""
Agency utilities for uploading catalog (csv or indiviudal)
By Sebastian Mora (@bastian1110)
"""
import csv
from pymongo import MongoClient
from requests import post


# Class for handling data upload to the database
class Reader:
    # Constructor that user the Mongo Connection string and target database
    def __init__(self, uri, sql_url, db_name, embed, sentencer):
        self.client = MongoClient(uri)
        self.sql_url = sql_url
        self.db = self.client[db_name]
        self.embed = embed
        self.sentencer = sentencer
        self.knowledge = []

    def read_row(self, row: dict, agency: str, make: str, view: dict):
        description = self.sentencer(row)
        row["vector"] = self.embed(description)
        row["agency"] = agency
        row["view"] = view
        row["marca"] = make
        row["estatus"] = "stock"
        self.knowledge.append(row)

    def push_to_db(self):
        collection = self.db["autos"]
        result = collection.insert_many(self.knowledge)
        inserted_ids = result.inserted_ids
        counter = 0
        for i in inserted_ids:
            response = post(self.sql_url, json={"id_car": str(i)})
            if response.ok:
                counter += 1
            else:
                print("Request failed with status code:", response.text)

        print(f"{len(self.knowledge)} rows inserted in NO SQL DB")
        print(f"{counter} rows inserted in SQL DB")


if __name__ == "__main__":
    from utils import embed, make_sentence

    my_reader = Reader(
        "mongodb://localhost:27017",
        "https://sql.wheelwise.xyz/api/car",
        "test",
        embed,
        make_sentence,
    )
    with open("test.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            my_reader.read_row(row, 0, "Ford", {"test": 1})
    my_reader.push_to_db()

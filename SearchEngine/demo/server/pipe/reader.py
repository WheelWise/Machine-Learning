"""
Agency utilities for uploading catalog (csv or indiviudal)
By Sebastian Mora (@bastian1110)
"""
import csv
from utils import embed, make_sentence


# Class for handling data upload to the database
class Reader:
    # Constructor that user the Mongo Connection string and target database
    def __init__(self, uri, db_name, embed, sentencer):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.embed = embed
        self.sentencer = sentencer
        self.knowledge = []

    def read_row(self, row: dict, agency: str):
        description = self.sentencer(row)
        row["vector"] = self.embed(description)
        row["agency"] = agency
        row["estatus"] = "stock"
        self.knowledge.append(row)

    def push_to_db(self):
        collection = self.db["autos"]
        collection.insert_many(self.knowledge)
        print(f"{len(self.knowledge)} rows inserted in DB")


if __name__ == "__main__":
    from pymongo import MongoClient

    my_reader = Reader("mongodb://localhost:27017", "test", embed, make_sentence)
    with open("test.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            my_reader.read_row(row, "0")
    my_reader.push_to_db()

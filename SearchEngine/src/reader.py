"""
Agency utilities for uploading catalog (csv or indiviudal)
By Sebastian Mora (@bastian1110)
"""
import csv
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# Sentence2Vec model from S-BERt
model = SentenceTransformer("all-mpnet-base-v2")


def embed(sentence: str) -> list:
    return model.encode([sentence])[0].tolist()


# Sentence creator function
def make_sentence(obj):
    values = []
    for key, value in obj.items():
        if isinstance(value, str):
            values.append(value.lower())
        elif isinstance(value, bool) and value:
            key = key.lower().replace("_", " ")
            values.append(key)
        elif isinstance(value, (int, float)):
            key = key.lower().replace("_", " ")
            values.append(f"{key} {value}")
    if len(values) >= 2:
        return " ".join(values)
    else:
        return "Could not generate sentence: missing make or model info"


# Class for handling data upload to the database
class Reader:
    # Constructor that user the Mongo Connection string and target database
    def __init__(self, uri, db_name, embed, sentencer):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.embed = embed
        self.sentencer = sentencer
        self.protected_names = ["modelo", "año"]

    # Function for reading a csv file conatining lots of cars
    def read_from_csv(self, path, agency) -> str:
        collection = self.db["autos"]
        with open(path, "r") as f:
            dict_reader = csv.DictReader(f)
            for field in self.protected_names:
                if field not in dict_reader.fieldnames:
                    return f"Error: missing field {field} in csv"
            n_objects = 0
            for row in dict_reader:
                description = self.sentencer(row)
                row["vector"] = self.embed(description)
                row["agency"] = agency  # This should be replaced with the SQL agency id
                collection.insert_one(row)
                n_objects += 1
            return f"Succesfully added {n_objects} objects to the database"


if __name__ == "__main__":
    my_reader = Reader("mongodb://localhost:27017", "test", embed, make_sentence)
    print(my_reader.read_from_csv("test.csv", "nissan"))

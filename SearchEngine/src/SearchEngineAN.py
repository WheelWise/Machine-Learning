"""
Search Engine using ANN(oy) algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from time import time

# Import the multilingual sentence encoder
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")


def embed(sentence: str) -> list:
    return model.encode([sentence])[0]


# Functions for reading the database and parsing the cars
from pymongo import MongoClient


def readDatabase(url: str, database: str, collection: str) -> list:
    client = MongoClient(url)
    database = client[database]
    col = database[collection]
    cursor = col.find({})
    data = []
    for document in cursor:
        data.append(document)
    return data


def carParser(car) -> str:
    words = []
    for key in car:
        if not isinstance(car[key], str):
            keyDescriber = " ".join(key.split("_"))
            words.append((keyDescriber + " " + str(car[key])).lower())
            continue
        words.append(car[key].lower())
    return " ".join(words[1:])


# Libaries for the SearchEngine model
import numpy as np
from annoy import AnnoyIndex


class SearchEngine:
    def __init__(self, embedder, preprocessor, dimensions: int):
        self.embedder = embedder
        self.preprocessor = preprocessor
        self.dimensions = dimensions
        self.model = AnnoyIndex(self.dimensions, "angular")

    def buildKnowledgeFromDb(self, database: list) -> None:
        start = time()
        for item in database:
            sentence = self.preprocessor(item)
            self.model.add_item(item["_id"], self.embedder(sentence))
        end = time()
        print(f"Time taken to process database : {end - start} seconds")

    def build(self, n_trees: int) -> None:
        start = time()
        self.model.build(n_trees)
        end = time()
        print(f"Time taken to build ann: {end - start} seconds")

    def unbuild(self) -> None:
        self.model.unbuild()

    def save(self, file: str) -> None:
        self.model.save(file)

    def load(self, file: str) -> None:
        self.model.load(file)

    def search(self, string, n) -> list:
        return self.model.get_nns_by_vector(self.embedder(string), n)


if __name__ == "__main__":
    database = readDatabase("mongodb://localhost:27017/", "test", "cars")
    mySearcher = SearchEngine(embed, carParser, 768)
    mySearcher.buildKnowledgeFromDb(database)
    mySearcher.build(100)
    mySearcher.save("./models/test.ann")
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")
        print("Resultado : ", mySearcher.search(test, 5))

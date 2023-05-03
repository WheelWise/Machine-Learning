"""
Search Engine using KNN algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from time import time

# Import the multilingual sentence encoder
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")


def embed(sentence: str):
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
import pickle
from sklearn.neighbors import NearestNeighbors


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, embedder, preprocessor, neigbors) -> None:
        self.model = NearestNeighbors(n_neighbors=neigbors, metric="cosine")
        self.embedder = embedder
        self.preprocessor = preprocessor
        self.knowledge = []

    # Fucntion to iterate over an array of objects, parse them and build knowledge
    def buildKnowledgeFromDb(self, database) -> None:
        start = time()
        for item in database:
            sentence = self.preprocessor(item)
            self.knowledge.append(np.array(self.embedder(sentence)))
        end = time()
        print(f"Time taken to process database : {end - start} seconds")

    # Fucntion to read one object, parse it and build knowledge
    def addKnowledge(self, item) -> None:
        pass

    # Function to train the knn model with the actual knowledge
    def fit(self) -> None:
        start = time()
        self.model.fit(self.knowledge)
        end = time()
        print(f"Time taken to build knn: {end - start} seconds")

    # Main function to make search over the db, it returns an array of indexes of the db
    def search(self, string) -> list:
        res = []
        embeded = np.array(self.embedder(string.lower()))
        distances, indices = self.model.kneighbors([embeded])
        for i in range(len(indices[0])):
            res.append(indices[0][i] + 1)
        return res


if __name__ == "__main__":
    # Lines to instatiate the functions and objects described before
    database = readDatabase("mongodb://localhost:27017/", "test", "cars")
    mySearcher = SearchEngine(embed, carParser, 10)
    mySearcher.buildKnowledgeFromDb(database)
    mySearcher.fit()
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() != "y":
            break
        test = input("Busqueda : ")
        print("Resultado : ", mySearcher.search(test))

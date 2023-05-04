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


# Libaries for the SearchEngine model
from pymongo import MongoClient
import numpy as np
import pickle
from sklearn.neighbors import NearestNeighbors


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, embedder, neigbors) -> None:
        self.model = NearestNeighbors(n_neighbors=neigbors, metric="cosine")
        self.embedder = embedder
        self.indexes = {}
        self.knowledge = []
        self.knowledge_size = 0

    # Fucntion to iterate over an array of objects and build knowledge
    def get_knowledge(self, url: str, database: str) -> None:
        start = time()
        client = MongoClient(url)
        database = client[database]
        collection = database["autos"]
        documents = collection.find({"estado": "stock"}, {"_id": 1, "vector": 1})
        for document in documents:
            self.knowledge.append(np.array(document["vector"]))
            self.indexes[self.knowledge_size] = document["_id"]
            self.knowledge_size += 1
        end = time()
        print(f"Total : {self.knowledge_size} added in {end-start} seconds")

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
            res.append(self.indexes[indices[0][i]])
        return res


if __name__ == "__main__":
    # Lines to instatiate the functions and objects described before
    my_searcher = SearchEngine(embed, 10)
    my_searcher.get_knowledge("mongodb://localhost:27017", "test")
    my_searcher.fit()
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")
        print("Resultado : ", my_searcher.search(test))

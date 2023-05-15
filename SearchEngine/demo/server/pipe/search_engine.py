"""
Search Engine using KNN algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from time import time


# Libaries for the SearchEngine model
import numpy as np
from utils import embed
from sklearn.neighbors import NearestNeighbors


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, embedder) -> None:
        self.model = None
        self.embedder = embedder

    def build(self, documents, neighbors) -> None:
        start = time()
        self.indexes = {}
        knowledge = []
        knowledge_size = 0
        for document in documents:
            knowledge.append(np.array(document["vector"]))
            self.indexes[knowledge_size] = document["_id"]
            knowledge_size += 1
        end = time()
        print(f"Total : {knowledge_size} added in {end-start} seconds")
        self.model = NearestNeighbors(n_neighbors=neighbors, metric="cosine")
        start = time()
        self.model.fit(knowledge)
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
    from pymongo import MongoClient

    my_searcher = SearchEngine(embed)
    client = MongoClient("mongodb://localhost:27017")
    database = client["test"]
    collection = database["autos"]
    documents = collection.find({"estatus": "stock"}, {"_id": 1, "vector": 1})
    my_searcher.build(documents, 3)
    # _id: { $in: []}
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")
        print("Resultado : ", my_searcher.search(test))

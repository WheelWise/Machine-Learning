"""
Search Engine using KNN algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from time import time
from pymongo import MongoClient

# Libaries for the SearchEngine model
import numpy as np
from sklearn.neighbors import NearestNeighbors


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, uri, db_name, embedder) -> None:
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["autos"]
        self.model = None
        self.embedder = embedder
        self.knowledge = []
        self.knowledge_size = 0

    def build(self, neighbors) -> None:
        start = time()
        documents = self.collection.find({"estatus": "stock"}, {"_id": 1, "vector": 1})
        self.indexes = {}
        self.knowledge = []
        self.knowledge_size = 0
        for document in documents:
            self.knowledge.append(np.array(document["vector"]))
            self.indexes[self.knowledge_size] = document["_id"]
            self.knowledge_size += 1
        end = time()
        print(f"Total : {self.knowledge_size} added in {end-start} seconds")
        self.model = NearestNeighbors(n_neighbors=neighbors, metric="cosine")
        start = time()
        if len(self.knowledge) > 0:
            self.model.fit(self.knowledge)
            end = time()
            print(f"Time taken to build knn: {end - start} seconds")

    # Main function to make search over the db, it returns an array of indexes of the db
    def search(self, string) -> list:
        if self.knowledge_size != 0:
            res = []
            embeded = np.array(self.embedder(string.lower()))
            distances, indices = self.model.kneighbors([embeded])
            for i in range(len(indices[0])):
                res.append(self.indexes[indices[0][i]])
            results = self.collection.find(
                {"_id": {"$in": res}}, {"vector": 0, "estatus": 0}
            )
            documents = []
            for document in results:
                document["_id"] = str(document["_id"])
                documents.append(document)
            return documents
        return []


if __name__ == "__main__":
    # Lines to instatiate the functions and objects described before
    from utils import embed

    my_searcher = SearchEngine("mongodb://localhost:27017", "test", embed)
    my_searcher.build(3)
    # _id: { $in: []}
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")
        print("Resultado : ", my_searcher.search(test))

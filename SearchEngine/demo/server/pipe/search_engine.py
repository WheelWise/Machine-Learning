"""
Search Engine using Cosine Similarity and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from sentence_transformers.util import cos_sim
from pymongo import MongoClient


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, uri, db_name, embedder) -> None:
        self.client = MongoClient(uri)
        self.collection = self.client[db_name]["autos"]
        self.embedder = embedder

    def search(self, string, n):
        if string:
            data = self.collection.find({"estatus": "stock"})
            index = {}
            embeddings = []
            counter = 0
            for doc in data:
                embeddings.append(doc["vector"])
                doc.pop("vector")
                index[counter] = doc
                counter += 1

            test = self.embedder(string)
            scores = cos_sim([test], embeddings).tolist()[0]

            similarity = []
            for i in range(len(scores) - 1):
                similarity.append({"object": index[i], "score": scores[i]})

            similarity = sorted(similarity, key=lambda x: x["score"], reverse=True)

            result = []
            for i in range(n):
                doc = similarity[i]["object"]
                doc["_id"] = str(doc["_id"])
                result.append(doc)
            return result
        return []


if __name__ == "__main__":
    from utils import embed

    my_searcher = SearchEngine("mongodb://localhost:27017", "wheelwise", embed)
    # _id: { $in: []}
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")

        # print("Resultado : ", my_searcher.search(test))
        my_searcher.search(test, 10)

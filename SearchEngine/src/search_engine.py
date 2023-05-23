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

    def search(self, string):
        if string:
            documents = self.collection.find(
                {"estatus": "stock"}, {"_id": 1, "vector": 1}
            )
            index = {}
            embeddings = []
            counter = 0
            for doc in documents:
                index[counter] = doc["_id"]
                embeddings.append(doc["vector"])
                counter += 1

            test = self.embedder(string)
            scores = cos_sim([test], embeddings).tolist()[0]

            result = []
            for i in range(len(scores) - 1):
                result.append({"index": i, "score": scores[i]})

            result = sorted(result, key=lambda x: x["score"], reverse=True)

            final = []
            x = 0
            for res in result:
                if x < 20:
                    final.append(index[res["index"]])
                    x += 1

            final_result = self.collection.find(
                {"_id": {"$in": final}}, {"vector": 0, "estatus": 0}
            )

            final_documents = []
            for document in final_result:
                document["_id"] = str(document["_id"])
                final_documents.append(document)
            return final_documents
        return []


if __name__ == "__main__":
    from utils import embed

    my_searcher = SearchEngineCos("mongodb://localhost:27017", "wheelwise", embed)
    # _id: { $in: []}
    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() == "n":
            break
        test = input("Busqueda : ")
        print("Resultado : ", my_searcher.search(test))

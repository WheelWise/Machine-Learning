"""
WW Search Engine Server Demo
By : Sebastian Mora
"""

# Import the multilingual sentence encoder
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")


def embed(sentence: str) -> list:
    return model.encode([sentence])[0]


# Libaries for creating the server

from flask import Flask, request, jsonify
from flask_cors import CORS
from SearchEngineAN import SearchEngine, carParser
from pymongo import MongoClient

app = Flask("Search Engine Demo")
cors = CORS(app)

mySearcher = SearchEngine(embed, carParser, 768)
mySearcher.load("../../src/models/tt.ann")

client = MongoClient("mongodb://localhost:27017/")
database = client["test"]
col = database["cars"]


def returnCars(ids):
    res = []
    for id in ids:
        cursor = col.find({"_id": id})
        for item in cursor:
            res.append(item)
    return res


@app.route("/search", methods=["POST", "GET"])
def search():
    string = request.values.get("s")
    if not string:
        return jsonify({"message": "No string search received"}), 400
    neighbors = mySearcher.search(string, 10)
    searchResults = returnCars(neighbors)
    return (
        jsonify({"cars": searchResults}),
        200,
    )


if __name__ == "__main__":
    app.run(host="localhost", port=8080)

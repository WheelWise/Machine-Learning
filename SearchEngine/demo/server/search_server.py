""" 
WW Search Engine Search Server 
By : Sebastian Mora (@bastian1110)
"""

from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pipe.search_engine import SearchEngine
from pipe.utils import embed
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

load_dotenv()

DATABASE_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("TARGET_DB")

searcher = SearchEngine(DATABASE_URI, DATABASE_NAME, embed)
searcher.build(15)


@app.route("/update", methods=["POST"])
def updateModel():
    neighbors = request.values.get("neighbors")
    if not neighbors:
        neighbors = 15
    try:
        searcher.build(int(neighbors))
        return jsonify({"message": "Model trained!", "error": False}), 200
    except:
        return jsonify({"message": "Error fitting the model", "error": True}), 500


@app.route("/search", methods=["POST"])
def search():
    string = request.values.get("search")
    if not string:
        return jsonify({"message": "No string search received", "error": True}), 400
    try:
        result = searcher.search(string)
        return (
            jsonify(
                {
                    "message": "Success",
                    "cars": result,
                    "error": False,
                }
            ),
            200,
        )
    except:
        return (
            jsonify(
                {
                    "message": "Error getting data from the model",
                    "error": True,
                }
            ),
            500,
        )


if __name__ == "__main__":
    app.run(port=8082, debug=True)

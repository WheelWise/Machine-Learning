""" 
WW Search Engine Search Server 
By : Sebastian Mora (@bastian1110)
"""

from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pipe.search_engine import SearchEngine
from pipe.utils import embed
from car_api import CarApi
from dotenv import load_dotenv
import os

search_server = Flask(__name__)
search_server.config["SECRET_KEY"] = "secret!"
search_server.config["CORS_HEADERS"] = "Content-Type"
CORS(search_server)

load_dotenv()

DATABASE_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("TARGET_DB")

searcher = SearchEngine(DATABASE_URI, DATABASE_NAME, embed)
api = CarApi(DATABASE_URI, DATABASE_NAME)


@search_server.route("/search", methods=["POST"])
def search():
    string = request.values.get("search")
    n_cars = request.values.get("n_cars")
    if not string:
        return jsonify({"message": "No string search received", "error": True}), 400
    if not n_cars:
        n_cars = 30
    try:
        result = searcher.search(string, n_cars)
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
                    "cars": [],
                    "error": True,
                }
            ),
            500,
        )


@search_server.route("/cars", methods=["GET", "POST"])
def cars():
    if request.method == "GET":
        try:
            cars = api.get_all()
            return jsonify({"message": "Success", "cars": cars, "error": False}), 200
        except:
            return jsonify({"message": "Failed", "cars": [], "error": False}), 500
    if request.method == "POST":
        try:
            car_id = request.values.get("id")
            if not car_id:
                return (
                    jsonify(
                        {"message": "No car id recieved", "cars": [], "error": True}
                    ),
                    400,
                )

            cars = api.get_one(car_id)
            return jsonify({"message": "Success", "cars": cars, "error": False}), 200
        except:
            return jsonify({"message": "Failed", "cars": [], "error": False}), 500


@search_server.route("/cars/agency", methods=["POST"])
def carsByAgency():
    agency_id = request.values.get("id")
    if not agency_id:
        return (
            jsonify({"message": "No agency id recieved", "cars": [], "error": True}),
            400,
        )
    try:
        cars = api.get_agency(agency_id)
        return jsonify({"message": "Success", "cars": cars, "error": False}), 200
    except:
        return jsonify({"message": "Failed", "cars": [], "error": False}), 500


@search_server.route("/cars/branch", methods=["POST"])
def carsByBranch():
    branch_id = request.values.get("id")
    if not branch_id:
        return (
            jsonify({"message": "No branch id recieved", "cars": [], "error": True}),
            400,
        )
    try:
        cars = api.get_branch(branch_id)
        return jsonify({"message": "Success", "cars": cars, "error": False}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed", "cars": [], "error": False}), 500


@search_server.route("/cars/make", methods=["POST"])
def carsByMake():
    make_id = request.values.get("id")
    if not make_id:
        return (
            jsonify({"message": "No make id recieved", "cars": [], "error": True}),
            400,
        )
    try:
        cars = api.get_make(make_id)
        return jsonify({"message": "Success", "cars": cars, "error": False}), 200
    except:
        return jsonify({"message": "Failed", "cars": [], "error": False}), 500


@search_server.route("/fullTextSearch", methods=["POST"])
def full_text_search():
    string = request.values.get("search")
    if not string:
        return jsonify({"message": "No string search received", "error": True}), 400
    try:
        cars = api.search(string)
        return jsonify({"message": "Success", "cars": cars, "error": False}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed", "cars": [], "error": False}), 500


if __name__ == "__main__":
    search_server.run(host="0.0.0.0", port=8084)

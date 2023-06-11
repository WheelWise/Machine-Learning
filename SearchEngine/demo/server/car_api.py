from pymongo import MongoClient
from bson import ObjectId


class CarApi:
    def __init__(self, uri, db_name) -> None:
        self.client = MongoClient(uri)
        self.collection = self.client[db_name]["autos"]

    def search(self, query):
        result = list(
            self.collection.aggregate(
                [
                    {
                        "$search": {
                            "index": "autoIndex",
                            "text": {
                                "query": query,
                                "path": {"wildcard": "*"},
                                "fuzzy": {"maxEdits": 2, "prefixLength": 0},
                            },
                        }
                    },
                    {"$project": {"vector": 0}},
                ]
            )
        )
        for document in result:
            document["_id"] = str(document["_id"])
        return result

    def get_all(self):
        cars = []
        documents = self.collection.find({}, {"vector": 0})
        for document in documents:
            document["_id"] = str(document["_id"])
            cars.append(document)
        return cars

    def get_one(self, id):
        cars = []
        documents = self.collection.find({"_id": ObjectId(id)}, {"vector": 0})
        for document in documents:
            document["_id"] = str(document["_id"])
            cars.append(document)
        return cars

    def get_make(self, make):
        cars = []
        documents = self.collection.find({"marca": make}, {"vector": 0})
        for document in documents:
            document["_id"] = str(document["_id"])
            cars.append(document)
        return cars

    def get_agency(self, agency):
        cars = []
        documents = self.collection.find({"agency": int(agency)}, {"vector": 0})
        for document in documents:
            document["_id"] = str(document["_id"])
            cars.append(document)
        return cars

    def get_branch(self, branch):
        cars = []
        documents = self.collection.find({"branch": int(branch)}, {"vector": 0})
        for document in documents:
            document["_id"] = str(document["_id"])
            cars.append(document)
        return cars

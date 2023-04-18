"""
Search Engine using KNN algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""

# Import the multilingual sentence encoder
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")


def embed(sentence: str) -> list:
    return modelSpanish.encode([sentence])[0]


# Functios for reading the database and parsing the cars
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


def carParser(car):
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
from sklearn.neighbors import NearestNeighbors


class SearchEngine:
    # Constructor that accepts the embedder (imported from tf_hub, function to parse the cars and how many neigbors )
    def __init__(self, embedder, preprocessor, neighbors) -> None:
        self.embedder = embedder
        self.knowledge = []
        self.knowledgeSize = 0
        self.labels = []
        self.model = NearestNeighbors(n_neighbors=neighbors, metric="cosine")
        self.preprocessor = preprocessor

    # Fucntion to iterate over an array of objects, parse them and build knowledge
    def buildKnowledgeFromDb(self, database) -> None:
        for item in database:
            sentence = self.preprocessor(item)
            self.knowledge.append(np.array(self.embedder(sentence)))
            self.labels.append(self.knowledgeSize)
            self.knowledgeSize += 1

    # Fucntion to read one object, parse it and build knowledge
    def addKnowledge(self, item) -> None:
        id, sentence = self.preprocessor(item)
        self.knowledge.append(np.array(self.embedder(sentence)))
        self.labels.append(id)

    # Function to train the knn model with the actual knowledge
    def fit(self) -> None:
        self.model.fit(self.knowledge)

    # Main function to make search over the db, it returns an array of indexes of the db
    def search(self, string) -> list:
        res = []
        embeded = np.array(self.embedder(string.lower()))
        distances, indices = self.model.kneighbors([embeded])
        for i in range(len(indices[0])):
            res.append(indices[0][i] + 1)
        return res


x = readDatabase("mongodb://localhost:27017/", "Test", "cars")
for i in x:
    print(carParser(i))

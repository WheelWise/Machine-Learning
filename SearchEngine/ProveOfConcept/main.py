""" 
Natural Language Search Engine Concept
By : Sebastian Mora (@bastian1110)
"""

# Import the 'universal sentende encoder' model from tensorflow hub
# This model is the embedder we are going to use
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Libaries to read json, knn model and n-dimensional arrays
import json
# pip install numpy
import numpy as np
from sklearn.neighbors import NearestNeighbors

#import preprocessing
import preprocessing


# Function to read each object of the databse file and convert it to a dictionary
def readDatabase(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        if isinstance(data, dict):
            return [data]
        elif isinstance(data, list):
            return data
        else:
            raise ValueError(
                "Databse file must contain a JSON object or an array of JSON objects"
            )


# Fucntion to build a string that summarize the car object you pass as an argument
def carParser(car):
    words = []
    for key in car:
        if not isinstance(car[key], str):
            words.append((key + " " + str(car[key])).lower())
            continue
        words.append(car[key].lower())
    return " ".join(words[1:])


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
            self.knowledge.append(np.array(embed([sentence]))[0])
            self.labels.append(self.knowledgeSize)
            self.knowledgeSize += 1

    # Fucntion to read one object, parse it and build knowledge
    def addKnowledge(self, item) -> None:
        id, sentence = self.preprocessor(item)
        self.knowledge.append(np.array(embed([sentence]))[0])
        self.labels.append(id)

    # Function to train the knn model with the actual knowledge
    def fit(self) -> None:
        self.model.fit(self.knowledge)

    # Main function to make search over the db, it returns an array of indexes of the db
    def search(self, string) -> list:
        res = []
        embeded = np.array(self.embedder([string.lower()]))[0]
        distances, indices = self.model.kneighbors([embeded])
        for i in range(len(indices[0])):
            res.append(indices[0][i] + 1)
        return res


def main():
    # Lines to use the functions and objects described before
    database = readDatabase("./database.json")
    mySearcher = SearchEngine(embed, carParser, 3)
    mySearcher.buildKnowledgeFromDb(database)
    mySearcher.fit()
    
    prompt = input("Search: ")
    prompt = preprocessing.transform_prompt(prompt)

    # Search function usage
    print(mySearcher.search(prompt))
if __name__ == "__main__":
    main()


"""
Search Engine using ANN(oy) algorithm and sentence embedding
By : Sebastian Mora (@bastian1110)
"""
from annoy import AnnoyIndex

# Functions for reading the database and parsing the cars
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


def carParser(car) -> str:
    words = []
    for key in car:
        if not isinstance(car[key], str):
            keyDescriber = " ".join(key.split("_"))
            words.append((keyDescriber + " " + str(car[key])).lower())
            continue
        words.append(car[key].lower())
    return " ".join(words[1:])


from sentence_transformers import SentenceTransformer


def embed(sentence: str):
    return model.encode([sentence])[0]


if __name__ == "__main__":
    # Lines to instatiate the functions and objects described before
    model = SentenceTransformer("all-mpnet-base-v2")
    database = readDatabase("mongodb://localhost:27017/", "Test", "cars")
    sentences = []
    for car in database:
        sentences.append(carParser(car))

    myAnnoy = AnnoyIndex(768, "angular")

    for i in range(1, len(sentences) + 1):
        embedded = embed(sentences[i - 1])
        myAnnoy.add_item(i, embedded)

    myAnnoy.build(10)
    myAnnoy.save("annoytest.ann")

    while True:
        answer = input("New Search ? (Y/n) ")
        if answer.lower() != "y":
            break
        test = input("Busqueda : ")
        print("Resultado : ", myAnnoy.get_nns_by_vector(embed(test), 3))

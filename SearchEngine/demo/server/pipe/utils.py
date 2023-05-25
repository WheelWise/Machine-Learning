"""
Functions that are shared between models. 
By : Sebastian Mora (@bastian1110)
"""
from json import load
from sentence_transformers import SentenceTransformer

# Sentence2Vec model from S-BERt
with open("tags.json") as f:
    tags = load(f)


model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")


def embed(sentence: str) -> list:
    return model.encode([sentence])[0].tolist()


# Sentence creator function
def make_sentence(obj):
    special_keys = ["modelo", "año", "precio", "marca", "color"]
    image_names = ["imagen", "url", "image", "foto"]
    values = []
    car_info = {}
    for key, value in obj.items():
        if key not in image_names:
            if key in special_keys:
                car_info[key] = value
            else:
                try:
                    value = int(value)
                except:
                    pass
                if isinstance(value, str):
                    values.append(value.lower())
                elif isinstance(value, bool) and value:
                    key = key.lower().replace("_", " ")
                    values.append(key)
                elif isinstance(value, (int, float)):
                    key = key.lower().replace("_", " ")
                    values.append(f"{key} {value}")
    try:
        model_tags = tags[obj["modelo"].lower()]
    except:
        model_tags = []
        pass

    result = "Es un vehiculo"
    for tag in model_tags:
        result += " " + tag
    result += ", el cual cuenta con :"
    for value in values:
        result += " " + value
    result += ". Asi es el "
    for key, value in car_info.items():
        result += f"{key} {value} "
    if len(values) >= 2:
        return result
    else:
        return ""


if __name__ == "__main__":
    import csv

    with open("miau.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            print(make_sentence(row))

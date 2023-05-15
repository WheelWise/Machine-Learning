"""
Functions that are shared between models. 
By : Sebastian Mora (@bastian1110)
"""
from sentence_transformers import SentenceTransformer

# Sentence2Vec model from S-BERt
model = SentenceTransformer("all-mpnet-base-v2")


def embed(sentence: str) -> list:
    return model.encode([sentence])[0].tolist()


# Sentence creator function
def make_sentence(obj):
    values = []
    for key, value in obj.items():
        if isinstance(value, str):
            values.append(value.lower())
        elif isinstance(value, bool) and value:
            key = key.lower().replace("_", " ")
            values.append(key)
        elif isinstance(value, (int, float)):
            key = key.lower().replace("_", " ")
            values.append(f"{key} {value}")
    if len(values) >= 2:
        return " ".join(values)
    else:
        return ""

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")


class Similarity:
    def __init__(self):
        self.model = model

    def embed(self, sentence: str) -> list:
        return self.model.encode([sentence])[0].tolist()

    def similarity(self, string, base):
        print("=" * 15)
        print(f"String : {string}")
        embeddings = self.model.encode(base, convert_to_tensor=True)

        cosine_scores = cos_sim([self.embed(string)], embeddings).tolist()[0]

        result = []
        for i in range(len(cosine_scores)):
            result.append({"index": i, "score": cosine_scores[i]})

        result = sorted(result, key=lambda x: x["score"], reverse=True)

        for i in result:
            print(f"{base[i['index']]} - {i['score']}")


import nltk
from nltk.corpus import wordnet as wn
from pymongo import MongoClient
nltk.download('wordnet')


class Mongo:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.knowledge = []

    def read_row(self, palabra: str, sinonimo: str):
        row = {"sinonimo": {sinonimo: palabra}}
        self.knowledge.append(row)

    def read_collection(self):
        collection = self.db["palabras_sinonimos"]
        cursor = collection.find({})
        synonyms = {}
        for document in cursor:
            synonyms.update(document['sinonimo'])
        return synonyms

    def push_to_db(self):
        collection = self.db["palabras_sinonimos"]
        collection.insert_many(self.knowledge)
        print(f"{len(self.knowledge)} rows inserted in DB")


class Transformation:
    def __init__(self):
        self.mongo = Mongo("mongodb://localhost:27017", "test")
        self.palabras_sinonimos = self.mongo.read_collection()

    def guardar_palabra_sinonimo(self, palabra, sinonimo):
        self.mongo.read_row(palabra, sinonimo)

    def push_db(self):
        self.mongo.push_to_db()

    def obtener_sinonimos(self, palabra):
        sinonimos = []
        for syn in wn.synsets(palabra, lang='spa'):
            for lemma in syn.lemmas('spa'):
                sinonimo = lemma.name()
                if sinonimo != palabra:
                    sinonimos.append(lemma.name())
        return sinonimos

    def first_load(self):
        with open("word_bank", 'r', encoding='utf-8') as f:
            palabras = f.read.splitlines()
            sinonimos_encontrados = {}
            for palabra in palabras:
                if palabra in self.palabras_sinonimos:
                    pass
                else:
                    sinonimos = self.obtener_sinonimos(palabra)
                    sinonimos_encontrados[palabra] = palabra
                    for sinonimo in sinonimos:
                        if sinonimo not in sinonimos_encontrados:
                            sinonimos_encontrados[sinonimo] = palabra

            if sinonimos_encontrados:
                for sinonimo, palabra in sinonimos_encontrados.items():
                    self.guardar_palabra_sinonimo(palabra, sinonimo)
                self.push_db()

    def transform(self, oracion):
        oracion_convertida = []
        sinonimos_encontrados = {}
        for palabra in oracion.split():
            if palabra in self.palabras_sinonimos:
                oracion_convertida.append(self.palabras_sinonimos[palabra])
                print('palabra encontrada en la base de datos')
            else:
                sinonimos = self.obtener_sinonimos(palabra)
                sinonimos_encontrados[palabra] = palabra
                for sinonimo in sinonimos:
                    if sinonimo not in sinonimos_encontrados:
                        sinonimos_encontrados[sinonimo] = palabra
                oracion_convertida.append(palabra)

        if sinonimos_encontrados:
            for sinonimo, palabra in sinonimos_encontrados.items():
                self.guardar_palabra_sinonimo(palabra, sinonimo)
            self.push_db()

        return ' '.join(oracion_convertida)


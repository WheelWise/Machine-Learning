"""
Word Transformation by Synonyms
By : Rodrigo Mendoza

    Packages to install:
        pip install nltk
        pip install pymongo
"""

import nltk
from nltk.corpus import wordnet as wn

import json

nltk.download('wordnet')


class Transformation:
    def __init__(self):
        self.archivo = 'palabras_sinonimos.json'
        self.word_bank = 'word_bank'
        self.diccionario = {}
        self.obtener_diccionario()

    def obtener_diccionario(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.diccionario = json.load(f)
        except FileNotFoundError:
            self.diccionario = {}

    def actualizar_archivo(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.diccionario, f, ensure_ascii=False, indent=2)
        self.obtener_diccionario()

    def obtener_sinonimos(self, palabra):
        sinonimos = []
        for syn in wn.synsets(palabra, lang="spa"):
            for lemma in syn.lemmas("spa"):
                sinonimo = lemma.name()
                if sinonimo != palabra:
                    sinonimos.append(lemma.name())
        return sinonimos

    def first_load(self):

        tags = '../demo/server/pipe/tags.json'
        with open(tags, 'r', encoding='utf-8') as f:
            diccionario = json.load(f)

        lista_palabras = []
        for llave, valor in diccionario.items():
            for palabra in valor:
                lista_palabras.append(palabra)

        lista_palabras = set(lista_palabras)
        for palabra in lista_palabras:
            if palabra in self.diccionario:
                pass
            else:
                sinonimos = self.obtener_sinonimos(palabra)
                self.diccionario[palabra] = palabra
                for sinonimo in sinonimos:
                    if sinonimo not in self.diccionario:
                        self.diccionario[sinonimo] = palabra
        self.actualizar_archivo()

        # with open("word_bank", 'r', encoding='utf-8') as f:
        #     palabras = f.read().splitlines()
        #     for palabra in palabras:
        #         if palabra in self.diccionario:
        #             pass
        #         else:
        #             sinonimos = self.obtener_sinonimos(palabra)
        #             self.diccionario[palabra] = palabra
        #             for sinonimo in sinonimos:
        #                 if sinonimo not in self.diccionario:
        #                     self.diccionario[sinonimo] = palabra
        #
        #     self.actualizar_archivo()


    def transform(self, oracion):
        oracion_convertida = []
        for palabra in oracion.split():
            # Si encuentra la palabra en la DB de sinonimos, la reemplaza por la palabra del banco de palabras

            if palabra in self.diccionario:
                oracion_convertida.append(self.diccionario[palabra])
                print('palabra encontrada en la base de datos')
            else:
                oracion_convertida.append(palabra)


        return ' '.join(oracion_convertida)


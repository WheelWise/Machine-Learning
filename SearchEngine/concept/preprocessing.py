""" 
Natural Language Preprocessing
By : Rodrigo Mendoza
"""


import re
# pip install googletrans==3.1.0a0
from googletrans import Translator
# lemmatisation
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download es_core_news_sm
import spacy
# stemming
# pip install nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk import download
# import nltk

# pip install pyspellchecker
from spellchecker import SpellChecker
# siguiente paso convertir de caracter a numerico (ex. cinco -> 5)
# text_to_num.py
import text_to_num


def transform_prompt(prompt):
    download('stopwords')
    prompt = strip_formatting(prompt)
    # prompt = translate_prompt(prompt)
    prompt = correct_spelling(prompt)
    prompt = lemmatize_prompt(prompt)
    prompt = remove_stopwords(prompt)
    prompt = convert_to_numeric(prompt)
    prompt = strip_formatting(prompt)

    return prompt


def strip_formatting(prompt):
    # exclude emails
    prompt = re.sub(r'\S*@\S*\s?', '', prompt)
    # Exclude mentions
    prompt = re.sub(r'@\S*\s?', '', prompt)
    # exclude urls
    prompt = re.sub(r'http\S+|www.\S+', '', prompt)
    # Exclude symbols or punctuations
    prompt = re.sub(
        r'\?|\\|\!|\"|\#|\$|\%|\&|\'|\[|\^|\||\,|\¿|\¡|\_|\=|\>|\[|\^|\`|\{|\}|\~|\[|\]|\*|\+|\@|\/|\-|\:|\?|\¡|\¿||\.|\\|\“|\”|\(|\)|\;|\’|\;|\`|\´|\-|\·|\<|\º|\ª',
        '', prompt)
    # Exclude special case symbol '\nd'
    prompt = re.sub(r'\nd', '', prompt)
    # Exclude special case symbol '\n'
    prompt = re.sub(r'\n', '', prompt)
    # Exclude cases of hashtags
    prompt = re.sub(r'\B(\#[a-zA-Z]+\b)(?!;)', '', prompt)

    # Lower Case process
    prompt = prompt.lower()
    # Eliminate words length <= 2
    prompt = re.sub(r'\b\w{1,2}\b', '', prompt)
    # quitar acentos
    prompt = re.sub(r'[áàäâ]', 'a', prompt)
    prompt = re.sub(r'[éèëê]', 'e', prompt)
    prompt = re.sub(r'[íìïî]', 'i', prompt)
    prompt = re.sub(r'[óòöô]', 'o', prompt)
    prompt = re.sub(r'[úùüû]', 'u', prompt)
    # Consider only alphanumeric

    prompt = re.sub(r'[^a-zA-Z0-9|\s|ñ]', '', prompt)

    return prompt


def translate_prompt(prompt):
    translator = Translator()
    prompt = translator.translate(prompt, dest='es').text
    return prompt.lower()


def stem_prompt(prompt):
    stemmer = SnowballStemmer('spanish')
    return stemmer.stem(prompt)


def lemmatize_prompt(prompt):
    nlp = spacy.load("es_core_news_sm")
    nlp_prompt = nlp(prompt)
    # open cars makes and models to excluse them from the lemmatization
    with open('car_makes.txt', 'r') as file:
        car_makes = file.read().splitlines()
    with open('car_models.txt', 'r') as file:
        car_models = file.read().splitlines()
    prompt = ' '.join([word.lemma_ if word.text not in car_makes + car_models else word.text for word in nlp_prompt])
    return prompt


def remove_stopwords(prompt):
    with open('spanish_stopwords.txt', 'r') as file:
        additional_stopwords = file.read().splitlines()
    additional_stopwords += ['querer', 'ser', 'encantar']
    words = re.findall(r'\w+', prompt, flags=re.UNICODE)
    important_words = []
    for word in words:
        if word not in stopwords.words('spanish') + additional_stopwords:
            important_words.append(word)
    prompt = ' '.join(important_words)
    return prompt


def correct_spelling(prompt):
    with open('car_makes.txt', 'r') as file:
        car_makes = file.read().splitlines()
    with open('car_models.txt', 'r') as file:
        car_models = file.read().splitlines()
    car_models_makes = car_makes + car_models
    list_of_words = prompt.split()
    spanish_spell_checker = SpellChecker(language='es')
    for word in list_of_words:
        if word not in car_models_makes:
            if spanish_spell_checker.correction(word) != word \
                    and spanish_spell_checker.correction(word) != '' \
                    and spanish_spell_checker.correction(word) is not None:
                prompt = prompt.replace(word, spanish_spell_checker.correction(word))

    return prompt


def convert_to_numeric(prompt):
    return text_to_num.text2num(prompt)


def main():
    print(transform_prompt('Quiero un carro rojo del año dos mil Nissan atlas'))
    # print(transform_prompt('un carro rojo'))


if __name__ == '__main__':
    main()
"""
Natural Language Preprocessing
By : Rodrigo Mendoza

    Packages to install:
        pip install googletrans==3.1.0a0
        pip install -U pip setuptools wheel
        pip install -U spacy
        python -m spacy download es_core_news_sm
        pip install nltk
        pip install pyspellchecker
"""
import re
from googletrans import Translator
import spacy
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk import download
from spellchecker import SpellChecker
import language_tool_python
import text_to_num
from functools import lru_cache
import timeit

# Download NLTK resources
download('stopwords')
SPANISH_STOPWORDS = stopwords.words('spanish')

# Load spaCy accurate model
# NLP = spacy.load('es_dep_news_trf')
# Load spaCy efficient model
NLP = spacy.load('es_core_news_sm')

# Load additional stopwords
with open('spanish_stopwords.txt', 'r') as file:
    ADDITIONAL_STOPWORDS = file.read().splitlines()
STOPWORDS = SPANISH_STOPWORDS + ADDITIONAL_STOPWORDS
TOOL = language_tool_python.LanguageTool('es-MX')

# Load car makes and models
with open('car_makes.txt', 'r') as file:
    car_makes = file.read().splitlines()
with open('car_models.txt', 'r') as file:
    car_models = file.read().splitlines()
CAR_MODEL_MAKES = car_makes + car_models

# Create spellchecker instance
SPANISH_SPELL_CHECKER = SpellChecker(language='es')

# Regex compilations for additional performance
EMAIL_PATTERN = re.compile(r'\S*@\S*\s?')
MENTION_PATTERN = re.compile(r'@\S*\s?')
URL_PATTERN = re.compile(r'http\S+|www.\S+')
# symbols_punctuations_pattern = re.compile(r'\?|\\|\!|\"|\#|\$|\%|\&|\'|\[|\^|\||\,|\¿|\¡|\_|\=|\>|\[|\^|\`|\{
# |\}|\~|\[|\]|\*|\+|\@|\/|\-|\:|\?|\¡|\¿||\.|\\|\“|\”|\(|\)|\;|\’|\;|\`|\´|\-|\·|\<|\º|\ª')
SYMBOL_PATTERN = re.compile(r'[^\w\sñ]')
SPECIAL_CASE_1 = re.compile(r'\nd')
SPECIAL_CASE_2 = re.compile(r'\n')
HASTAG_PATTERN = re.compile(r'\B(\#[a-zA-Z]+\b)(?!;)')
WORD_LENGTH_PATTERN = re.compile(r'\b(?!\d)\w{1,2}\b')
A_ACCENT_PATTERN = re.compile(r'[áàäâ]')
E_ACCENT_PATTERN = re.compile(r'[éèëê]')
I_ACCENT_PATTERN = re.compile(r'[íìïî]')
O_ACCENT_PATTERN = re.compile(r'[óòöô]')
U_ACCENT_PATTERN = re.compile(r'[úùüû]')
ALPHA_NUMERIC_PATTERN = re.compile(r'[^a-zA-Z\d|\s|ñ]')


@lru_cache(maxsize=None)
def transform_prompt(prompt):
    prompt = strip_formatting(prompt)
    # prompt = translate_prompt(prompt)
    prompt = correct_spelling(prompt)
    prompt = lemmatize_prompt(prompt)
    prompt = convert_to_numeric(prompt)
    prompt = remove_stopwords(prompt)
    prompt = strip_formatting(prompt)

    return prompt


def strip_formatting(prompt):
    prompt = prompt.lower()

    replace_to_word = [A_ACCENT_PATTERN, E_ACCENT_PATTERN, I_ACCENT_PATTERN, O_ACCENT_PATTERN, U_ACCENT_PATTERN]
    word_to_replace = ['a', 'e', 'i', 'o', 'u']
    for pattern in replace_to_word:
        prompt = pattern.sub(word_to_replace[replace_to_word.index(pattern)], prompt)

    replace_to_blank = [EMAIL_PATTERN, MENTION_PATTERN, URL_PATTERN, SYMBOL_PATTERN, SPECIAL_CASE_1, SPECIAL_CASE_2,
                        HASTAG_PATTERN, WORD_LENGTH_PATTERN, ALPHA_NUMERIC_PATTERN]
    for pattern in replace_to_blank:
        prompt = pattern.sub('', prompt)

    return prompt


def translate_prompt(prompt):
    translator = Translator()
    prompt = translator.translate(prompt, dest='es').text
    return prompt.lower()


def stem_prompt(prompt):
    stemmer = SnowballStemmer('spanish')
    return stemmer.stem(prompt)


def lemmatize_prompt(prompt):
    nlp_prompt = NLP(prompt)
    # open cars makes and models to excluse them from the lemmatization

    prompt = ' '.join([word.lemma_ if word.text not in CAR_MODEL_MAKES else word.text for word in nlp_prompt])
    return prompt


def remove_stopwords(prompt):
    words = re.findall(r'\w+', prompt, flags=re.UNICODE)
    important_words = (word for word in words if word not in STOPWORDS)
    prompt = ' '.join(important_words)
    return prompt


def correct_spelling(prompt):
    list_of_words = prompt.split()
    """corrections = {word: SPANISH_SPELL_CHECKER.correction(word) if SPANISH_SPELL_CHECKER.correction(word) is not None
                   else word for word in list_of_words if
                   word not in CAR_MODEL_MAKES}
    prompt = ' '.join([corrections.get(word, word) for word in list_of_words])"""

    corrections = {word: TOOL.correct(word) if TOOL.correct(word) is not None
    else word for word in list_of_words if
                   word not in CAR_MODEL_MAKES}
    prompt = ' '.join([corrections.get(word, word) for word in list_of_words])

    return prompt


def convert_to_numeric(prompt):
    return text_to_num.text2num(prompt)


def main():
    start = timeit.default_timer()

    print(transform_prompt(
        "Quiero un coche familiar que sea amplio y cómodo para viajes largos, con un sistema de entretenimiento para los pasajeros traseros y que sea de color azul."))

    stop = timeit.default_timer()

    print('Time: ', stop - start)


if __name__ == '__main__':
    main()

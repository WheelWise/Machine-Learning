"""
Natural Language Preprocessing
By : Rodrigo Mendoza

    Packages to install:
        pip install -U pip setuptools wheel
        pip install -U spacy
        python -m spacy download es_core_news_sm
        pip install nltk
        pip install pyspellchecker
"""
import re
import spacy
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk import download
import language_tool_python
import text_to_num
from functools import lru_cache
import timeit
from transformation import Transformation

# Download NLTK resources
download("stopwords")
SPANISH_STOPWORDS = stopwords.words("spanish")

# Load spaCy accurate model
# NLP = spacy.load('es_dep_news_trf')
# Load spaCy efficient model
import es_core_news_sm

NLP = es_core_news_sm.load()

# Load additional stopwords
with open("spanish_stopwords", "r", encoding="utf-8") as file:
    ADDITIONAL_STOPWORDS = file.read().splitlines()
STOPWORDS = SPANISH_STOPWORDS + ADDITIONAL_STOPWORDS
TOOL = language_tool_python.LanguageTool("es-MX")

with open("go_words", "r", encoding="utf-8") as file:
    go_words = file.read().splitlines()
GO_WORDS = go_words

# Regex compilations for additional performance
EMAIL_PATTERN = re.compile(r"\S*@\S*\s?")
MENTION_PATTERN = re.compile(r"@\S*\s?")
URL_PATTERN = re.compile(r"http\S+|www.\S+")
# symbols_punctuations_pattern = re.compile(r'\?|\\|\!|\"|\#|\$|\%|\&|\'|\[|\^|\||\,|\¿|\¡|\_|\=|\>|\[|\^|\`|\{
# |\}|\~|\[|\]|\*|\+|\@|\/|\-|\:|\?|\¡|\¿||\.|\\|\“|\”|\(|\)|\;|\’|\;|\`|\´|\-|\·|\<|\º|\ª')
SYMBOL_PATTERN = re.compile(r"[^\w\sñ]")
SPECIAL_CASE_1 = re.compile(r"\nd")
SPECIAL_CASE_2 = re.compile(r"\n")
HASTAG_PATTERN = re.compile(r"\B(\#[a-zA-Z]+\b)(?!;)")
WORD_LENGTH_PATTERN = re.compile(r"\b(?!\d)\w{1,2}\b")
A_ACCENT_PATTERN = re.compile(r"[áàäâ]")
E_ACCENT_PATTERN = re.compile(r"[éèëê]")
I_ACCENT_PATTERN = re.compile(r"[íìïî]")
O_ACCENT_PATTERN = re.compile(r"[óòöô]")
U_ACCENT_PATTERN = re.compile(r"[úùüû]")
ALPHA_NUMERIC_PATTERN = re.compile(r"[^a-zA-Z\d|\s|ñ]")


class Preprocessing:
    def __init__(self):
        self.prompt = ""
        self.transformation = Transformation()

    @lru_cache(maxsize=None)
    def transform_prompt(self, prompt):
        self.prompt = prompt
        self.remove_stopwords()
        self.correct_spelling()
        self.strip_formatting(False)
        self.transform()
        self.strip_formatting()
        self.lemmatize_prompt()
        self.stem_prompt()
        self.convert_to_numeric()
        self.strip_formatting()
        self.remove_stopwords()

        return self.prompt

    @lru_cache(maxsize=None)
    def transform_prompt_without_stem(self, prompt):
        self.prompt = prompt
        self.strip_formatting(False)
        self.correct_spelling()
        self.remove_stopwords()
        self.transform()
        self.strip_formatting()
        self.lemmatize_prompt()
        self.convert_to_numeric()
        self.strip_formatting()
        self.remove_stopwords()

        return self.prompt

    def transform(self):
        self.prompt = self.transformation.transform(self.prompt)

    def strip_formatting(self, remove_accents=True):
        self.prompt = self.prompt.lower()

        if remove_accents:
            replace_to_word = [
                A_ACCENT_PATTERN,
                E_ACCENT_PATTERN,
                I_ACCENT_PATTERN,
                O_ACCENT_PATTERN,
                U_ACCENT_PATTERN,
            ]
            word_to_replace = ["a", "e", "i", "o", "u"]
            for pattern in replace_to_word:
                self.prompt = pattern.sub(
                    word_to_replace[replace_to_word.index(pattern)], self.prompt
                )

        replace_to_blank = [
            EMAIL_PATTERN,
            MENTION_PATTERN,
            URL_PATTERN,
            SYMBOL_PATTERN,
            SPECIAL_CASE_1,
            SPECIAL_CASE_2,
            HASTAG_PATTERN,
            WORD_LENGTH_PATTERN
        ]
        if remove_accents:
            replace_to_blank.append(ALPHA_NUMERIC_PATTERN)

        for pattern in replace_to_blank:
            self.prompt = pattern.sub("", self.prompt)

    def stem_prompt(self):
        stemmer = SnowballStemmer("spanish")
        self.prompt = stemmer.stem(self.prompt)

    def lemmatize_prompt(self):
        nlp_prompt = NLP(self.prompt)
        # open cars makes and models to excluse them from the lemmatization

        self.prompt = " ".join(
            [
                word.lemma_ if word.text not in GO_WORDS else word.text
                for word in nlp_prompt
            ]
        )

    def remove_stopwords(self):
        words = re.findall(r"\w+", self.prompt, flags=re.UNICODE)
        important_words = (
            word for word in words if word not in STOPWORDS or word in GO_WORDS
        )
        self.prompt = " ".join(important_words)

    def correct_spelling(self):
        list_of_words = self.prompt.split()
        """corrections = {word: SPANISH_SPELL_CHECKER.correction(word) if SPANISH_SPELL_CHECKER.correction(word) is not None
                       else word for word in list_of_words if
                       word not in CAR_MODEL_MAKES}
        self.prompt = ' '.join([corrections.get(word, word) for word in list_of_words])"""

        corrections = {
            word: TOOL.correct(word) if TOOL.correct(word) is not None else word
            for word in list_of_words
            if word not in GO_WORDS
        }
        self.prompt = " ".join([corrections.get(word, word) for word in list_of_words])

    def convert_to_numeric(self):
        self.prompt = text_to_num.text2num(self.prompt)


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    prompt = "SUV mediano plateado con capacidad para siete pasajeros y tracción en las cuatro ruedas."
    prompt = Preprocessing().transform_prompt_without_stem(prompt)
    end = timeit.default_timer()
    print(prompt)
    print(end - start)
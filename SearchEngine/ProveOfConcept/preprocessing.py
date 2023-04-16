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
import nltk
nltk.download('stopwords')
# pip install pyspellchecker
from spellchecker import SpellChecker


def transform_prompt(prompt):
    prompt = strip_formatting(prompt)
    prompt = translate_prompt(prompt)
    prompt = correct_spelling(prompt)
    prompt = lemmatize_prompt(prompt)
    prompt = remove_stopwords(prompt)
    
    return prompt
    
    
def strip_formatting(prompt):
    #exclude emails
    prompt = re.sub(r'\S*@\S*\s?', '', prompt)
    #Exclude mentions
    prompt = re.sub(r'@\S*\s?' , '', prompt)
    #exclude urls
    prompt = re.sub(r'http\S+|www.\S+', '', prompt)
    #Exclude symbols or punctuations
    prompt = re.sub(r'\?|\\|\!|\"|\#|\$|\%|\&|\'|\[|\^|\||\,|\¿|\¡|\_|\=|\>|\[|\^|\`|\{|\}|\~|\[|\]|\*|\+|\@|\/|\-|\:|\?|\¡|\¿||\.|\\|\“|\”|\(|\)|\;|\’|\;|\`|\´|\-|\·|\<|\º|\ª' , '', prompt)
    #Exclude special case symbol '\nd'
    prompt = re.sub(r'\nd', '', prompt)
    #Exclude special case symbol '\n'
    prompt = re.sub(r'\n', '', prompt)
    #Exclude cases of hashtags
    prompt = re.sub(r'\B(\#[a-zA-Z]+\b)(?!;)', '', prompt)
    # Consider only alphanumeric
    prompt = re.sub(r'[^a-zA-Z0-9|\s]' , '', prompt)
    # Lower Case process
    prompt = prompt.lower()
    #Eliminate words length <= 2 
    prompt = re.sub(r'\b\w{1,2}\b', '', prompt)
    
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
    prompt = ' '.join([word.lemma_ for word in nlp_prompt])
    return prompt


def remove_stopwords(prompt):
    with open('spanish_stopwords.txt', 'r') as file:
        additional_stopwords = file.read().splitlines()
    additional_stopwords += ['querer', 'ser', 'encantar']
    words = re.findall(r'\w+', prompt,flags = re.UNICODE) 
    important_words=[]
    for word in words:
        if word not in stopwords.words('spanish') + additional_stopwords:
            important_words.append(word)
    prompt = ' '.join(important_words)
    return prompt


def correct_spelling(prompt):
    list_of_words = prompt.split()
    spanish_spell_checker = SpellChecker(language='es')
    for word in list_of_words:
        if spanish_spell_checker.correction(word) != word:
            prompt = prompt.replace(word, spanish_spell_checker.correction(word))
    
    return prompt
    
def main():
    ...


if __name__ == '__main__':
    print(transform_prompt('un carro rojo'))
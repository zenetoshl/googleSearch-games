from .constants import *
import nltk 
from nltk.stem import RSLPStemmer

def tokenize(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    return text

def stemming(text):
    stemmer = RSLPStemmer()
    newText = []
    for word in text:
        newText.append(stemmer.stem(word.lower()))
    return newText

def removeStopWords(text):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    newText = []
    for word in text:
        if word not in stopwords:
            newText.append(word)
    return newText

def removePonctuation(allWords):
    newAllWords = []
    for word in allWords:
        for p in ponctuation:
            if (p in word):
                word = word.replace(p, '')
            word = word.lower()
        if len(word) > 2:
            newAllWords.append(word)
    return newAllWords


def tester():
    frase = 'eu adoro ter aulas de python'
    frase = tokenize(frase)
    frase = stemming(frase)
    frase = removeStopWords(frase)
    print(frase)    
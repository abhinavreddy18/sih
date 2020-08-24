# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:54:11 2020

@author: meghana ganapa
"""

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

file=open("D:\Abhinav\sih\sih_positive.txt")
sentences=file.readlines()
punctuations="?:!.,;"

for sentence in sentences:
    sentence_words = nltk.word_tokenize(sentence)
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)

    print("{0:20}{1:20}".format("Word","Lemma"))
    for word in sentence_words:
        print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))

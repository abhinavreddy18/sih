# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:03:38 2020

@author: meghana ganapa
"""

import nltk
#call the nltk downloader
nltk.download()
file=open("D:\Abhinav\sih\sih_positive.txt")
my_lines_list=file.readlines()

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

for i in my_lines_list:
    print(i)
    print("Stemmed sentence")
    x=stemSentence(i)
    print(x)


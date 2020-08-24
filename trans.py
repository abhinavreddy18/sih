# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:18:00 2020

@author: Vasihnavi
"""

from googletrans import Translator
import random
import re

translator = Translator()
translated = translator.translate(['hello',  'తెలుగు వార్తలు' , 'हिन्दी में टाइप करें  ','안녕하세요','你好嗎'])
c=translator.detect(' हिन्दी में टाइप करें ')
inputstring='hello తెలుగు వార్తలు हिन्दी में टाइप करें  안녕하세요 你好嗎 '
l=inputstring.split()
for i in l:
    print(translator.detect(i))
print(re.split(r'([a-zA-Z]+)',inputstring))
for t in translated:
    print(t.text,"",end='')
#print(translated.src)
#print(translated.pronunciation)
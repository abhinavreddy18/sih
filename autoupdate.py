import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
sid=SentimentIntensityAnalyzer()
import csv
data=pd.read_csv("D:\Abhinav\database.csv",index_col="hindi")


while(True):
    s=input("enter the statement")
    l=s.split()
    pos=0
    neg=0
    neu=0
    conv=""
    for i in l:
        try:
            des=data.loc[i].at['english']
            print(des)
            conv=conv+" "+des  
        except KeyError:
            continue
    print(conv)   
    senti=sid.polarity_scores(conv)
    pos=senti['pos']
    neg=+senti['neg']
    neu=senti['neu']
    print(pos," positive")
    print(neg," negative")
    print(neu," neutral")

        
        
        
        

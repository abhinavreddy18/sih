import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
sid=SentimentIntensityAnalyzer()

s=input("enetr the anlaysis")
print(sid.polarity_scores(s))
s=input("enter the statement")
l=s.split()
for i in l:
    s=sid.polarity_scores(i)
    print(s['neg'])


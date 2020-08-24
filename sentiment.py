import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
sid=SentimentIntensityAnalyzer()

s=input("enetr the anlaysis")
print(sid.polarity_scores(s))
print(sid.polarity_scores("i am happy"))

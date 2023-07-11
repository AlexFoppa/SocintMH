from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_polarity(text):
   analizer = SentimentIntensityAnalyzer()
   score = analizer.polarity_scores(text)
      
   if score['compound'] > 0:
      return("Sentimento positivo")
   elif score['compound'] < 0:
      return("Sentimento negativo")
   else:
      return("Sentimento neutro")
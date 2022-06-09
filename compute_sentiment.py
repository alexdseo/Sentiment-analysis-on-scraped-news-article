import pandas as pd
import json
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Models when using gpu
# from flair.models import TextClassifier
# from flair.data import Sentence
# from happytransformer import HappyTextClassification


def textblob(text):
    tb_clf = TextBlob(text)
    sentiment_tb = tb_clf.sentiment.polarity
    # Additional parameter TextBlob provides: Subjectivity of the text
    # subjectivity = tb_clf.sentiment.subjectivity

    return sentiment_tb


def vader(text):
    vd_clf = SentimentIntensityAnalyzer()

    sentiment_vd = vd_clf.polarity_scores(text)['compound']
    # Additional parameters Vader provide
    # negativity = vd_clf.polarity_scores(text)['neg']
    # neutrality = vd_clf.polarity_scores(text)['neu']
    # positivity = vd_clf.polarity_scores(text)['pos']

    return sentiment_vd


def write_sentiment(json_file):
    file = open(json_file)
    # Create Dataframe
    sentiments = pd.DataFrame()
    col_list = ['Date', 'Model', 'Sentiment']
    for i in file:
        article = json.loads(i)
        # Text components from the article
        header = str(article['title'] + '. ' + article['sub_title'])
        texts = str(article['title'] + '. ' + article['sub_title'] + article['main_article'])
        date = str(article['publish_date'])
        # Sentiment scores +1: positive, -1: negative
        score_v = vader(header)  # Only use Title and Sub-title
        score_t = textblob(texts)  # Use Title, Sub-title, and main article
        # Write dataframe consisting Text components
        temp = [[date, 'Vader', score_v], [date, 'TextBlob', score_t]]
        temp_df = pd.DataFrame(temp, columns=col_list)
        sentiments = pd.concat([sentiments, temp_df], ignore_index=True)

    return sentiments


if __name__ == '__main__':
    # JSON file created from scrape_news.py
    articles = 'recent_articles.json'
    # Write dataframe with sentiment score of each article using different models
    senti = write_sentiment(articles)
    # Export csv file
    senti.to_csv('sentiments.csv', encoding='utf-8', index=False)

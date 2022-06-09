# Sentiment-analysis-on-scraped-news-article

## Workflow

### 1. Web-scrapping & Pre-processing

`scrape_news.py`

- In this python script we build webscraper for specific [website](https://www.aljazeera.com/where/mozambique/), in order to get the texts from the 10 most recent articles. Since this is a very simple webscrapper, we use `BeautifulSoup4` library after exploring the HTML elements to find the urls for the 10 most recent article. After getting all the urls from the HTML elements, we save those urls for the recent articles into a list. Next, we take this list of urls and scrape all the texts from the article. While doing so, we only try to scrape the text of the article, removing anything that is not part of the article itself. Additionally, we perform simple pre-process the text data, removing unnecessary white space and strings at the end of the article. Finally, we save this dictionary of texts from each article into a `.json` file.

  - Output: 'recent_articles.json'

### 2. Sentiment Analysis

`compute_sentiment.py`

- In this python script, we implement few of the sentiment analysis model that is widely used. We use `VADER (Valence Aware Dictionary and sEntiment Reasoner)` and `TextBlob` here, while we will use bigger language models using gpu via GoogleColab on next step. From the json file we created on the prior step, we combine (Title and Subtitle) and define it as a *header*, and combine (Title, Subtitle, an Main body) and define it as a *texts*. We save the date of the article separatly for later visualization task. As `VADER` is pre-trained and performs much better for social communication texts such as twitter posts, we use `VADER` to calculate the sentiment score for the *header* with a shorter length of texts. We will use `TextBlob` to calculate the sentiment score for the *texts* with a longer length. Finally, we save the date of the article, the sentiment score and the corresponding model into a dataframe using `pandas`.

  - Input: `recent_articles.json`
  - Output: `sentiments.csv`

### 3. Visualization

`Sentiment_Analysis_gpu.ipynb`

- In this notebook, we implement larger language model, `Flair` and `DistilBERT(via huggingface api)` to caluclate sentiment of the article. We use *header* as an input data for `DistilBERT(via huggingface api)` due to api limit, but use *texts* as an input data for `Flair`. Then, we save the date of the article, the sentiment score and the corresponding model into a dataframe using `pandas` like prior step. Finally, we create a very simple line chart using `plotly`, taking 'Date' on x-axis and 'Sentiment' on y-axis.  
  
  - Input: `recent_articles.json`
  - Output: `sentiments_gpu.csv`

#### Line chart of the Sentiment analysis via plotly
![alt text](https://github.com/alexdseo/Sentiment-analysis-on-scraped-news-article/blob/master/simple_plotly.png)

- Looking at the line chart of sentiment scores using different model and different dataset we could find few insights. As we only used 10 datasets, we can review the 10 article and see if the language models' sentiment analysis were correct. Overall, we find that a larger language models, `Flair & DistilBERT`, did a better job on making correct sentiment analysis. However, we can also note that some of the article's title's sentiment and their entire text's sentiment can be different. 
- Next, we can also compare models that used same dataset. The models, `VADER & DistilBERT`, that used *header* datset, which only includes the title and the subtitle, largely agreed on most cases. However, they did very differently for few articles, such as [this article](https://www.aljazeera.com/news/2021/6/23/southern-african-nations-agree-to-deploy-forces-to-mozambique). As the subtitle includes words like 'terrorism' and 'violent extremism', the smaller model `VADER` predicted as a negative sentiment. However, `DistilBERT` predicted as positive sentiment, which is correct since the sentences actually means that other countries will help Mozambique to fight the 'terrorism'.
- Finally, for the model that used the entire texts of the article, `TextBlob & Flair`, we can definitely see that smaller model, `TextBlob`, did very poorly, contrast to `Flair`. While, `TextBlob` is very useful model to analyze the sentiment of the texts, it is also more suitable for shorter texts.

## Quickstart

1. Set up your environment. You can either use your base environment or create a conda virtual environment. Assuming anaconda is installed and using Python 3.8+:


```
conda create -n venv
conda activate venv
```

2. Set working directory:
`cd (To this repository)`

3. Install requirements:
```
conda install pip
pip install -r requirements-gpu.txt
```

4. Run Python scripts:
```
python scrape_news.py
python compute_sentiment.py
```

5. Then, run the gpu version on notebook above to get the sentiment scores of additional models and simple visualization using plotly.

- Sentiment Analysis and Visaulize on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alexdseo/Sentiment-analysis-on-scraped-news-article/blob/master/Sentiment_Analysis_gpu.ipynb)

*All python scripts written in PEP8 style*

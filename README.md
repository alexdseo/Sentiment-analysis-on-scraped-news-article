# Sentiment-analysis-on-scraped-news-article

## Workflow

### 1. Web-scrapping & Pre-processing

`scrape_news.py`

- Output:

### 2. Sentiment Analysis

`compute_sentiment.py`

- Input: `data_resized` (see Google Drive for all files; sample on GitHub)
- Output: `raw_text` (see Google Drive for all files; sample on GitHub)

### 3. Visualization

Sentiment Analysis and Visaulize on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com//https://github.com/alexdseo/Sentiment-analysis-on-scraped-news-article/blob/master/Sentiment_Analysis_gpu.ipynb)

- In this notebook 

## Quickstart

1. Set up your environment. Here's the easy way, assuming anaconda is installed:

```
conda create -y -n venv && conda activate venv && pip install -r requirements-gpu.txt
```

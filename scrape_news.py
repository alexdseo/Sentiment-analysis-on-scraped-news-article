import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json


def get_urls(target_website):
    # Request website page
    page = requests.get(target_website)
    # Parse HTML elements
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find(id='root')
    # Find all elements with recent articles
    h3 = elements.find_all("h3", class_="gc__title")
    # Create list to store url of each article
    urls = []
    # Scrape all urls of recent article
    for title in h3:
        link = title.find_all("a")
        for url in link:
            link_url = url["href"]
            article_type = link_url.split("/")[1]
            # Save only articles with texts, 'program' only includes video
            if article_type != 'program':
                urls.append('https://www.aljazeera.com' + link_url)

    return urls


def get_articles(urls):
    # Create list to store texts in articles
    recent_articles = []
    # Scrape all texts from 10 recent article 
    for i in tqdm(range(10)):
        # Request website page
        page= requests.get(urls[i])
        # Parse HTML elements
        soup = BeautifulSoup(page.content, 'html.parser')
        texts = soup.find_all(text=True)
        # Create dictionary for scrapped text
        article_texts = {'title': ''.join([t for t in texts if t.parent.name == 'h1']).replace('\n', ' '),
                         'sub_title': ''.join([t for t in texts if t.parent.name == 'em']).replace('\n', ' '),
                         'publish_date': '-'.join(urls[i].split('/')[4:7]),
                         'main_article': ''.join([t for t in texts if t.parent.name == 'p']).replace('\n', ' ').replace(
                             'Follow Al Jazeera English:', '')}
        # Additional text from the article: image caption
        # article_texts['image_caption'] = ''.join([t for t in texts if t.parent.name=='figcaption']).replace('\n',' ')
        
        recent_articles.append(article_texts)
        pass

    return recent_articles


if __name__ == '__main__':
    # Specific website given for this task
    website = "https://www.aljazeera.com/where/mozambique/"
    # Get list of url of recent articles
    url_lst = get_urls(website)
    # Scrape article from the web, removing anything that is not part of the article itself
    article_lst = get_articles(url_lst)
    # Write json file
    with open('recent_articles.json', 'w', encoding='utf-8') as f:
        for item in article_lst:
            f.write(json.dumps(item) + "\n")

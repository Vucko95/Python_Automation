import os
from re import U
from webbrowser import get
import requests
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()  # for python-dotenv method


news_api_key = os.environ.get('news_api_key')


def get_news(country, category, api_key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f"TITLE\n', {article['title']}, 'ARTICLE_BRO\n', {article['description']}")
    return results


print(get_news(country='de', category='business', api_key=news_api_key))

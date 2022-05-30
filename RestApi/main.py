# import re
# from urllib import request
import requests

r = requests.get(
    'https://newsapi.org/v2/top-headlines?country=us&apiKey=a7ff35c98b8e4653aab38851e722b226')
content = r.json()
articles = content['articles']
# print(type(articles))
for article in articles:
    print('TITLE\n', article['title'], 'ARTICLE_BRO\n', article['description'])
    print("---------------")

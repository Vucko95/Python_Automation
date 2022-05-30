from webbrowser import get
import requests

# r = requests.get(
#     'https://newsapi.org/v2/top-headlines?country=us&apiKey=a7ff35c98b8e4653aab38851e722b226')
# content = r.json()
# articles = content['articles']
# for article in articles:
#     print('TITLE\n', article['title'], 'ARTICLE_BRO\n', article['description'])
#     print("---------------")
# de business


def get_news(country, category, api_key='a7ff35c98b8e4653aab38851e722b226'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f"TITLE\n', {article['title']}, 'ARTICLE_BRO\n', {article['description']}")
    return results


print(get_news(country='de', category='business'))

import requests
import json

r = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=983e60a50ff45ccd9208c225c13db7b2')
content = r.json()
with open('./RestApi/weather.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=4)
# weather = content['weather']
# print(weather)
# print(content)

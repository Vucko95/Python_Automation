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


def check_city_temp(city_name, api_key='983e60a50ff45ccd9208c225c13db7b2'):
    city = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}')
    city_content = city.json()
    with open('./RestApi/city.json', 'w', encoding='utf-8') as f:
        json.dump(city_content, f, ensure_ascii=False, indent=4)
    return city_content


check_city_temp(city_name='Dublin')
# // todo users inputs City name and it saves as that name of city

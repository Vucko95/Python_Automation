import requests
import json
r = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=983e60a50ff45ccd9208c225c13db7b2')
content = r.json()
with open('./RestApi/weather.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=4)


def check_city_temp(city_name, api_key='983e60a50ff45ccd9208c225c13db7b2'):
    city = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}')
    city_content = city.json()
    with open(f'./RestApi/{city_name}.json', 'w', encoding='utf-8') as f:
        json.dump(city_content, f, ensure_ascii=False, indent=4)
    return city_content


print("Please input City Name")
city_name = input()
check_city_temp(city_name)

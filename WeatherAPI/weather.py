import requests
import json
import os
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()  # for python-dotenv method


weather_api_key = os.environ.get('weather_api_key')
r = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={weather_api_key}')
content = r.json()
with open('./WeatherApi/weather.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=4)


def check_city_temp(city_name, api_key=weather_api_key):
    city = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}')
    city_content = city.json()
    with open(f'./RestApi/{city_name}.json', 'w', encoding='utf-8') as f:
        json.dump(city_content, f, ensure_ascii=False, indent=4)
    return city_content


# print("Please input City Name")
# city_name = input()
# check_city_temp(city_name)


# apikey = ''


# def get_file_contents(apikey):
#     try:
#         with open('./WeatherAPI/apikey.txt', 'r') as f:
#             # It's assumed our file contains a single line,
#             # with our API key
#             return f.read().strip()
#     except FileNotFoundError:
#         print("'%s' file not found" % apikey)


# api_key = get_file_contents(apikey)
# print("Our API key is: %s" % (api_key))

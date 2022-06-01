import requests
import os
import json
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()  # for python-dotenv method


token = os.environ.get('fb_token')
url = f'https://graph.facebook.com/v14.0/me?fields=id%2Cname%2Cposts&access_token={token}'
response = requests.get(url)
print(response)
print(response.text)
# ALWAYS var.content to output actual INFO Not only 200

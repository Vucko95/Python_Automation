import requests
import os
import json
url = 'https://api.languagetool.org/v2/check'

data = {
    'text': 'Thix is nixe day',
    'language': 'auto'
}

response = requests.post(url, data=data)
result = json.loads(response.text)
with open(f'./LanguagePOST/result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

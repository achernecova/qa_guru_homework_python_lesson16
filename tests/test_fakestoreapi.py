import json
import sys

import requests



def test_api():
    resource = requests.get("https://preprod.softmg.ru/api/v2/cases")
    print("Привет")
    if resource.status_code == 200:
        data = resource.json()
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
    else:
        print(f"Ошибка запроса: {resource.status_code}")


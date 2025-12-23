import json

import requests


def test_api_softmg():
    resource = requests.get("https://preprod.softmg.ru/api/v2/cases")
    print("Привет")
    if resource.status_code == 200:
        data = resource.json()
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
    else:
        raise ValueError(f"Ошибка запроса: {resource.status_code}")

import requests

inputs = {"text1": "Sport Bags - Puma", "text2": "35", "text3": "Female"}

headers = {'content-type': 'application/json'}

url = "http://127.0.0.1:5000/item_recommendation"

r = requests.post(url=url, json=inputs, headers=headers)
print(r)

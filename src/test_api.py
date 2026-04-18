import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "steps": 5,
    "Holiday": [0,1,0,0,1],
    "Discount": [0.1,0.2,0.1,0.05,0.3]
}

response = requests.post(url, json=data)
print(response.json())
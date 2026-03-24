import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "features": [1,5,99,5,4,9,99]
}

response = requests.post(url, json=data)

print(response.json())
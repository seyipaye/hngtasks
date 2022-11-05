import requests

endpoint = "http://127.0.0.1:8000/api/"
# endpoints = "https://httpbin.org/anything"

response = requests.post(endpoint, json={'message': 'This is a real fresh message'}, params= {'abc': 123})
print(response.json())
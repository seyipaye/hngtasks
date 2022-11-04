import requests

endpoints = "http://127.0.0.1:8000/"
# endpoints = "https://httpbin.org/anything"

response = requests.get(endpoints)
print(response.json())
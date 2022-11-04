import requests

endpoints = "https://httpbin.org/status/200/"
endpoints = "https://httpbin.org/anything"

response = requests.get(endpoints)
print(response.json)
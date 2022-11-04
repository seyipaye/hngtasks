import requests

endpoints = "https://httpbin.org/status/200/"
endpoints = "https://httpbin.org"

response = requests.get(endpoints)
print(response.text)
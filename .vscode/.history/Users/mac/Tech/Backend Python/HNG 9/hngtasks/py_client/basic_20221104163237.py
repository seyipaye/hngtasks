import requests

endpoints = "https://httpbin.org/status/200/"
endpoints = "https://httpbin.org/anything"

response = requests.get(endpoints, json= {'hello': 'How you dey'})
print(response.json())
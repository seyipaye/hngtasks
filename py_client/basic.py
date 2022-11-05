import requests

endpoint = "http://127.0.0.1:8000/api/"
#endpoint = "https://seyi-hng.herokuapp.com/api/"

# endpoints = "https://httpbin.org/anything"

response = requests.post(endpoint, json={'message': 'This is a real freshhhhh message'}, params= {'abc': 123})
print(response.json())
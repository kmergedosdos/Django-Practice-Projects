import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title": "hello worldsss"}) # Http get request

# print(get_response.text) #print raw text
# print(get_response.status_code)

print(get_response.json())
# print(get_response.status_code)
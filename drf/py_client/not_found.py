import requests

endpoint = "http://localhost:8000/api/products/1234/"

get_response = requests.get(endpoint) # Http get request

print(get_response.json())
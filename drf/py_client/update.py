import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
  "id": 1,
  "title": "hello blog",
  "price": 100
}

get_response = requests.put(endpoint, json=data) # Http get request

print(get_response.json())
import requests

endpoint = "http://localhost:8000/api/products/"

data = {
  "title": "hello blog"
}

headers = {'Authorization': 'Bearer ab561b3878bb9b48ea7364e7f12b8a790aeeec6c'}

get_response = requests.post(endpoint, json=data, headers=headers) # Http get request

print(get_response.json())
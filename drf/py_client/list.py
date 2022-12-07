import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter username: ")
password = getpass("Enter password: ")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password}) # Http get request

print(auth_response.json())


if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    "Authorization": f"Bearer {token}"
  }

  endpoint = "http://localhost:8000/api/products/"

  get_response = requests.get(endpoint, headers=headers) # Http get request

  print(get_response.json())
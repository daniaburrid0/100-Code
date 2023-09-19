import requests

pixela_endpoint = "https://pixe.la/v1/users"
use_parameters = {
    "token": "thisissecret",
    "username": "daniaburrid0",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=use_parameters)

print(response.text)
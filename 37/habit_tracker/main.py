import requests
import datetime as dt

TOKEN = "thisissecret"
USERNAME = "daniaburrid0"

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_parameters = {
    "id": "coding1",
    "name": "Daly Coding Graph",
    "unit": "lines",
    "type": "int",
    "color": "ajisai",
}

user_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, headers=user_headers, json=graph_parameters)
# print(response.text)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/coding1"
pixel_parameters = {
    "date": "20230916",
    "quantity": "100",
}

# response = requests.post(url=pixel_endpoint, headers=user_headers, json=pixel_parameters)
# print(response.text)

pixel_put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/coding1/20230916"
pixel_put_parameters = {
    "quantity": "200",
}

response = requests.put(url=pixel_put_endpoint, headers=user_headers, json=pixel_put_parameters)
print(response.text)
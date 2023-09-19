import requests as rq
import json
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")

API_KEY = os.environ.get("API_KEY")

SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

TOKEN = os.environ.get("TOKEN")

def user_response() -> str:
    """Ask user for input"""
    user_input = input("Please enter workout: ")
    return user_input

def nutritionix_response(user_input: str) -> str:
    # headers
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    # endpoint
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    # parameters
    parameters = {
        "query": user_input,
    }
    # make the request
    response = rq.post(endpoint, json=parameters, headers=headers)
    return response.json()
    
def save_to_file(response: str, name: str) -> None:
    with open(f'{name}.json', 'w') as file:
        json.dump(response, file, indent=4)
        
def make_new_row(row_dict: dict) -> None:
    endpoint = SHEET_ENDPOINT
    header = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    parameters = {
        "workout": {
            "date": row_dict["Date"],
            "time": row_dict["Time"],
            "exercise": row_dict["Exercise"],
            "duration": row_dict["Duration"],
            "calories": row_dict["Calories"]
        }
    }
    response = rq.post(endpoint, json=parameters, headers=header)
    print(response.text) 

def main():
    # ask for user input
    user_input = user_response()
    # nutritionix response
    response = nutritionix_response(user_input)
    # save response to file
    save_to_file(response, user_input)
    row_dict = {}
    for d in response['exercises']:
        row_dict['Date'] = dt.datetime.now().strftime("%d/%m/%Y")
        row_dict['Time'] = dt.datetime.now().strftime("%H:%M:%S")
        row_dict['Exercise'] = d["name"].title()
        row_dict['Duration'] = d["duration_min"]
        row_dict['Calories'] = d["nf_calories"]
        make_new_row(row_dict)
    
if __name__ == '__main__':
    main()
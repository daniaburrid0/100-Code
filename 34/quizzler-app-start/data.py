# API link: https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean
import requests

try:
    api_response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
    api_response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")
else:
    question_data = api_response.json()["results"]
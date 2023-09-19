import os
import requests
import json
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


def get_stock_intraday() -> dict:
    endpoint = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK,
        "interval": "60min",
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(endpoint, params=parameters)
    response.raise_for_status()
    return response.json()


def save_to_file(data: dict, file_name: str):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def get_info_stock():
    try:
        data = get_stock_intraday()
        save_to_file(data, "stock.json")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        day_before_yesterday = (
            datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        yesterday_close = data["Time Series (60min)"][yesterday +
                                                      " 19:00:00"]["4. close"]
        day_before_yesterday_close = data["Time Series (60min)"][day_before_yesterday +
                                                                 " 19:00:00"]["4. close"]
        difference = float(yesterday_close) - float(day_before_yesterday_close)
        percentage = (difference / float(day_before_yesterday_close)) * 100
        print_percentage_and_news(percentage)
    except requests.exceptions.HTTPError as e:
        print(f"Error getting stock data: {e}")


def get_news() -> dict:
    endpoint = "https://newsapi.org/v2/everything"
    parameters = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(endpoint, params=parameters)
    response.raise_for_status()
    return response.json()


def get_3_top_news():
    try:
        data = get_news()
        save_to_file(data, "news.json")
        for i in range(3):
            title = data['articles'][i]['title']
            brief = data['articles'][i]['description']
            print(f"Title: {title}\nBrief: {brief}\n")
    except requests.exceptions.HTTPError as e:
        print(f"Error getting news data: {e}")


def print_percentage_and_news(percentage: float):
    if percentage > 0:
        print(f"{STOCK}: 🔺{percentage:.2f}%")
    else:
        print(f"{STOCK}: 🔻{percentage:.2f}%")
    get_3_top_news()


def main():
    get_info_stock()


if __name__ == "__main__":
    main()
import requests
from datetime import datetime
import time
from config import MY_LAT, MY_LONG

def fetch_iss_position():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None, None
    data = response.json()
    return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])

def fetch_sun_timing():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None, None
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset

while True:
    iss_latitude, iss_longitude = fetch_iss_position()
    sunrise, sunset = fetch_sun_timing()

    time_now = datetime.now().hour
    
    if iss_latitude is not None and iss_longitude is not None:
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            if time_now >= sunset or time_now <= sunrise:
                print("Look up!")
            else:
                print("It's day time")
        else:
            print("It's not close to you")
    time.sleep(60)

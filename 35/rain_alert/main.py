from os import environ
import requests

loc = {
    "lat": -32.411569,
    "lon": -63.243765,
}

def main():
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params={
        "lat": loc["lat"],
        "lon": loc["lon"],
        "appid": environ["OWM_API_KEY"],
        "exclude": "current,minutely,daily",
        "units": "metric",
    })
    response.raise_for_status()
    print(response.status_code)
    data = response.json()
    # save the data to a file and make it readable
    with open("weather_data.json", "w") as file:
        file.write(str(data))
    weather_slice = data["hourly"][:12]
    will_rain = False
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        print("Bring an umbrella.")
    else:
        print("No rain today.")

if __name__ == "__main__":
    main()
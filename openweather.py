# openweather.py
import requests

def get_weather_summary(lat, lon, date, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    try:
        response = requests.get(url)
        data = response.json()
        summary = {
            "condition": data["weather"][0]["description"].title(),
            "temp": data["main"]["temp"],
            "wind_speed": data["wind"]["speed"]
        }
        return summary
    except Exception as e:
        print("Error fetching OpenWeather data:", e)
        return {"condition": "Unavailable", "temp": "--", "wind_speed": "--"}

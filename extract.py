import requests
import pandas as pd

API_KEY = "0094f6265d03e7033e1ed6782b345c36"
CITY = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

data = requests.get(url).json()

weather_data = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"]
}

df = pd.DataFrame([weather_data])

print(df)
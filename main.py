import requests
import pandas as pd
import mysql.connector
from datetime import datetime


API_KEY = "0094f6265d03e7033e1ed6782b345c36"
CITY = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(url)
data = response.json()


weather_data = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"],
    "timestamp": datetime.now()
}

df = pd.DataFrame([weather_data])

print("Data Extracted:")
print(df)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manoj@3459",
    database="weather_db"
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    weather VARCHAR(50),
    timestamp DATETIME
)
""")

# Insert data
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, weather, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()

print("Data loaded into MySQL successfully!")
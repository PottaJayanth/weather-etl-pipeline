import mysql.connector
import pandas as pd

df = pd.DataFrame([{
    "city": "Hyderabad",
    "temperature": 30,
    "humidity": 60,
    "weather": "clear sky"
}])

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manoj@3459",
    database="weather_db"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, weather)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()

print("Data inserted!")
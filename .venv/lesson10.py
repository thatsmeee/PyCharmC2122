import sqlite3
import requests
from bs4 import BeautifulSoup
import time

def create_database():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather
                 (date TEXT, time TEXT, temperature REAL)''')
    conn.commit()
    conn.close()

def weather():
    url = "https://weather.com/weather/tenday/l/Dnipro+Dnipropetrovsk+Oblast+Ukraine?canonicalCityId=8432a18768331578baf183adf7822026be696f2e878ee445bf6f5049371a03e2"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature_div = soup.find("div", class_="DailyContent--temp--1s3a7 DailyContent--tempN--33RmW")
    if temperature_div:
        temperature = temperature_div.text.strip()
        return temperature
    else:
        return None

def insert_data_into_database(date, time, temperature):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))
    conn.commit()
    conn.close()

create_database()
while True:
    try:
        temperature = weather()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        date, time_now = current_time.split()
        insert_data_into_database(date, time_now, temperature)
        print(f"Weather data for {date} at {time_now}: Temperature {temperature}°C")
        time.sleep(1800)
    except Exception as e:
        print("Error:", e)

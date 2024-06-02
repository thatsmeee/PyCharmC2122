import requests
from bs4 import BeautifulSoup
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DateWeather:
    def __init__(self, date, temperature, precipitation, wind_speed, wind_direction):
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def __repr__(self):
        return (f"DateWeather(date={self.date}, temperature={self.temperature}, "
                f"precipitation={self.precipitation}, wind_speed={self.wind_speed}, "
                f"wind_direction={self.wind_direction})")


def fetch_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        weather_date = soup.find('div', class_='weather-date')
        weather_temp = soup.find('div', class_='weather-temperature')
        weather_opa = soup.find('div', class_='weather-precipitation')
        weather_spewin = soup.find('div', class_='weather-wind-speed')
        weather_locwin = soup.find('div', class_='weather-wind-destination')

        return DateWeather(weather_date, weather_temp, weather_opa, weather_spewin, weather_locwin)

    except requests.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None
    except AttributeError as e:
        logging.error(f"Error parsing weather data: {e}")
        return None


def insert_weather_data(cursor, weather_data):
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            date TEXT,
            temperature TEXT,
            precipitation TEXT,
            wind_speed TEXT,
            wind_direction TEXT
        )
        ''')
        cursor.execute('''INSERT INTO weather (date, temperature, precipitation, wind_speed, wind_direction)
                          VALUES (?, ?, ?, ?, ?)''',
                       (
                       weather_data.date, weather_data.temperature, weather_data.precipitation, weather_data.wind_speed,
                       weather_data.wind_direction))
        return True
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return False


def fetch_weather_by_date(cursor, date):
    try:
        cursor.execute("SELECT * FROM weather WHERE date = ?", (date,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []


def fetch_extreme_temperature(cursor, order):
    try:
        cursor.execute(f"SELECT * FROM weather ORDER BY temperature {order} LIMIT 1")
        return cursor.fetchone()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return None


def main():
    url = 'https://thatsmeee.github.io/weather/'
    weather_data = fetch_weather_data(url)

    if weather_data:
        conn = sqlite3.connect('weather_data.db')
        cursor = conn.cursor()

        if insert_weather_data(cursor, weather_data):
            logging.info("Weather data inserted successfully.")

            specified_date = '02.06.2024'
            data_by_date = fetch_weather_by_date(cursor, specified_date)

            weather_records = [DateWeather(date=row[0], temperature=row[1], precipitation=row[2], wind_speed=row[3],
                                           wind_direction=row[4])
                               for row in data_by_date]

            logging.info(f"Data for date {specified_date}: {weather_records}")

            lowest_temp_data = fetch_extreme_temperature(cursor, 'ASC')
            logging.info(f"Data for lowest temperature: {lowest_temp_data}")

            highest_temp_data = fetch_extreme_temperature(cursor, 'DESC')
            logging.info(f"Data for highest temperature: {highest_temp_data}")

        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()

import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        # pprint(data)  # FIX: Drop with error, because waiting for API key will be activate

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"The weather in {city_name}\nTemperature: {temperature}\nHumidity: {humidity}\nWind Speed: {wind_speed} m/s")

    except Exception as ex:
        print(ex)
        print('Check your city name')

def main():
    city = input('Enter your city: ')
    get_weather(city, open_weather_token)

if __name__ == "__main__":
    main()

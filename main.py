import requests
from pprint import pprint
from config import open_weather_token

def get_weather (city, open_weather_token):


    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Check it out by opening the window)"

        country = data["sys"]["country"]
        wind = data["wind"]["speed"]

        print(f"Weather in city: {city}\n Temperature: {cur_weather}C° {wd}\n"
              f"Country: {country}\n Wind: {wind} m/s\n"
              f"Have a nice day!")

    except Exception as ex:
        print(ex)
        print("Check the city name")

def main():
    city = input("Enter city: ")
    get_weather(city, open_weather_token)

if __name__ == "__main__":
    main()
import urllib.request
import json
import sys


def get_woeid(city):
    f = urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={city}")
    if f.status == 200:
        data = f.read()
        data = json.loads(data)
        if not data:
            print("Nie ma takiego miasta:", city)
            exit(1)
        woeid = data[0]['woeid']
    else:
        print("Błąd pobierania")
        exit(1)

    return woeid


def get_weather_data(woeid):
    f = urllib.request.urlopen(f"https://www.metaweather.com/api/location/{woeid}")
    if f.status == 200:
        data = f.read()
        data = json.loads(data)
        weather = data['consolidated_weather']
        weather_today = weather
        return weather_today[0]
    else:
        print("Błąd pobierania")
        exit(1)

def print_weather(weather, city):
    print(f"Pogoda w {city} w dniu {weather['applicable_date']}:")
    print(f" - opis: {weather['weather_state_name']}")
    print(f" - temperatura: {weather['the_temp']}°C")
    print(f" - ciśnienie: {weather['air_pressure']}hPa")
    print(f" - wilgotność: {weather['humidity']}%")


city = sys.argv[1]
print_weather(get_weather_data(get_woeid(city)), city)
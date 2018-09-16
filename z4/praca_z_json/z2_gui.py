import urllib.request
import json
import sys
import tkinter

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

def print_weather_gui():
    city = miasto_entry.get()
    weather = get_weather_data(get_woeid(city))

    wynik1_label.configure(text=f"Opis: {weather['weather_state_name']}")
    wynik2_label.configure(text=f"Temperatura: {weather['the_temp']}°C")
    wynik3_label.configure(text=f"Wilgotność: {weather['humidity']}%")
    wynik4_label.configure(text=f"Ciśnienie: {weather['air_pressure']}hPa")


# city = sys.argv[1]
# print_weather(get_weather_data(get_woeid(city)), city)

root = tkinter.Tk()
root.title("Sprawdz pogodę")

miasto_label = tkinter.Label(master=root, text="Wpisz miasto")
miasto_label.pack()
# a_label.grid(row=0, column=0)
miasto_entry = tkinter.Entry(master=root)
miasto_entry.pack()

dodaj_button = tkinter.Button(master=root, text="Dodaj", command=print_weather_gui)
dodaj_button.pack()

wynik1_label = tkinter.Label(master=root, text="Ciśnienie: ")
wynik1_label.pack()
wynik2_label = tkinter.Label(master=root, text="Temperatura: ")
wynik2_label.pack()
wynik3_label = tkinter.Label(master=root, text="Wilgotnosc: ")
wynik3_label.pack()
wynik4_label = tkinter.Label(master=root, text="Ciśnienie: ")
wynik4_label.pack()


root.mainloop()


import json

file = "baza_pracownikow.json"

def pobierz_dane_pracownika():
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_urodz = input("Rok urodzenia: ")
    pensja = input("Pensja: ")
    return [imie, nazwisko, rok_urodz, pensja]


def zapisz(baza):
    # zapis do pliku
    with open(file, "w") as f:
        json.dump(baza, f)


def odczyt():
    # otwarcie pliku
    try:
        with open(file) as f:
            baza = json.load(f)
    except FileNotFoundError:
        print("Pierwszy pracownik")
        baza = []

    return baza


def dodaj():
    baza = odczyt()
    pracownik = pobierz_dane_pracownika()
    baza.append(pracownik)
    zapisz(baza)


def wypisz():
    baza = odczyt()
    i = 0
    for pracownik in baza:
        i += 1
        print(f'- [{i}] {pracownik[0]}, {pracownik[1]}, - rok: {pracownik[2]}, pensja: {pracownik[3]}')


while True:
    akcja = input("Co chcesz zrobić [d - dodaj, w - wypisz, k - wyjscie] ")
    if akcja == "d":
        dodaj()
    elif akcja == "w":
        wypisz()
    elif akcja == "k":
        break
    else:
        print("Zła opcja!")
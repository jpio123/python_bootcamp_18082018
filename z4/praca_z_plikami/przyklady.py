plik = open("pliki_wejsciowe/dane.txt")
print(plik)
plik.close()

with open("pliki_wejsciowe/dane.txt") as plik:
    print(plik)
    print(plik.read())


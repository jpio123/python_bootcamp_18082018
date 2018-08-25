
napis = input("Podaj jakis napis: ")
samo = 0
SAMOGLOSKI = 'aeiouy'

for i in napis.lower():
    if i in SAMOGLOSKI:
        samo += 1

print(f'Liczba samogłosek: {samo}')

liczby = [11, 22, -33, 44, 500, -6, 77, 188, -99, 1010]
ile_dod = 0
ile_uj = 0
i = 0

while i < len(liczby):
    if liczby[i] >= 0:
        ile_dod += 1
    else:
        ile_uj += 1
    i += 1

print(f'Dodatnich jest {ile_dod} a ujemnych {ile_uj}')

# prościej:

lista = [11, 22, -33, 44, 500, -6, 77, 188, -99, 1010]
ile_dod = 0
ile_uj = 0

for liczba in lista:
    if liczba >= 0:
        ile_dod += 1
    else:
        ile_uj += 1


print(f'Dodatnich jest {ile_dod} a ujemnych {ile_uj}')

liczby = set()

while True:
    liczba = input('Podaj liczbę calkowita lub k zeby wyjsc: ')
    if liczba == 'k':
        break
    else:
        liczby.add(int(liczba))

print('Podales unikalne liczby: ', liczby)
print('Unikalych w sumie jest: ', len(liczby))

PARZYSTE = set(range(0,101,2))

print('Ile z nich jest parzystych: ', len(liczby & PARZYSTE))
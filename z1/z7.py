liczba = int(input('Podaj liczbę całkowitą: '))

# można bez nawiasów bo and silniejsze od or
print( (liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7)
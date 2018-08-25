

miasto_a = input('Podaj nazwę miasta A: ')
miasto_b = input('Podaj nazwę miasta B: ')
odleglosc = float(input(f'Podaj odległość {miasto_a}-{miasto_b}: '))
cena_paliwa = float(input('Podaj cenę paliwa: '))
spalanie = float(input('Podaj spalanie L/100km: '))

koszt = odleglosc/100 * spalanie * cena_paliwa

print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:} PLN')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {int(koszt)} PLN')
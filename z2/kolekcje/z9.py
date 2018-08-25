
cennik = {
    'ziemniory': 2.5,
    'pomodoro': 8,
    'marchewka': 3,
    'buraki': 4
}

stan = {
    'ziemniory': 10,
    'pomodoro': 10,
    'marchewka': 5,
    'buraki': 2
}
koszyk = {}

while True:
    print(f'Na stanie mamy jeszcze:')
    for i in stan:
        if stan[i] > 0:
            print(f' {i} ilosc: {stan[i]} kg, cena: {cennik[i]} zł')
    produkt = input('Podaj co chcesz kupic z dostępnych lub k zeby wyjsc: ')
    if produkt == 'k':
        break
    else:
        ilosc = float(input(f'Podaj ile kg {produkt} chcesz: '))
        if ilosc > stan[produkt]:
             print("Sorry, nie mam tyle")
        else:
            cena = cennik[produkt] * (ilosc)
            print(f'Do zapłaty będzie: {cena}\n\n')
            koszyk[produkt] = cena
            stan[produkt] -= ilosc

koszt_calk = 0
print("\nOto twój koszyk:")
for wklad in koszyk:
    koszt_calk += koszyk[wklad]
    print(f'{wklad} cena {koszyk[wklad]} PLN')

print(f'\nDo zapłaty za całość: {koszt_calk}')
print("\nZapraszamy ponownie")
liczba_1 = float(input('Podaj pierwsza liczbe: '))
liczba_2 = float(input('Podaj drugą licznę: '))
dzialanie = input('Wpisz znak dzialania: ')

if dzialanie == '+':
    print(f'Wynik: {liczba_1 + liczba_2}')
elif dzialanie == '-':
	print(f'Wynik: {liczba_1 - liczba_2}')
elif dzialanie == '*':	
	print(f'Wynik: {liczba_1 * liczba_2}')
elif dzialanie == '/':	
	print(f'Wynik: {liczba_1 / liczba_2}')
else:
	print('Zły rodzaj operacji')
	
if dzialanie == '+':
	wynik=liczba_1 + liczba_2    
elif dzialanie == '-':
	wynik=liczba_1 - liczba_2
elif dzialanie == '*':	
	wynik=liczba_1 * liczba_2
elif dzialanie == '/':	
	wynik=liczba_1 / liczba_2
else:
	# wynik = 'Zły rodzaj operacji'
	wynik = None

if wynik is not None:
    print(f'Wynik: {wynik}')
else:
    print('zla operacja')
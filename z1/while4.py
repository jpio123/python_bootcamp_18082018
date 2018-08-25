suma = 0
licznik = 0

while True:	
	liczba = input(f'Podaj liczbe calkowitą: ')
	if liczba == 'koniec':
		print(f'no to kończymy')
		break
	suma = suma + int(liczba)
	licznik += 1
	
print(f'Suma wszystkich liczb to: {suma}')
print(f'Liczba wszystkich liczb to: {licznik}')
print(f'Srednia wszystkich liczb to: {suma / licznik}')

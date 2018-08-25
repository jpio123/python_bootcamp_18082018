i = 0

while True:
	liczba = input('Podaj liczbe lub komendę koniec: ')
	if (liczba == 'koniec'):
		print(f'Narka')
		exit()
	elif liczba == '':
		print(f'Miała być liczba albo komenda "koniec"')
		continue
	else:
		liczba = int(liczba)
		if i == 0:
			min = liczba
			max = liczba
		else:
			if liczba > max:
				print(f'wieksza od max ({max})')
				max = liczba
			if liczba < min:
				print(f'mniejsza of min ({min})')
				min = liczba
	i =+ 1

print(f'Najwieksza: ({max})')
print(f'Najmniejsza: ({min})')	
	

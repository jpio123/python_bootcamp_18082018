x = int(input('Podaj pozycje x: '))
y = int(input('Podaj pozycje y: '))

print('\n###############################\n')

if 0 <= y < 10:
	if 0 <= x < 10:
		print('Lewy Gorny')
	elif x <= 90:
		print('Gorna krawedz')
	elif x <= 100:
		print('Prawy górny')
	else:
		print('Poza krawedzia')		
elif 10 < y <= 90:
	if 0 <= x < 10:
		print('Srodkowy Gorny')
	elif x <= 90:
		print('Centrum')
	elif x <= 100:
		print('Prawy srodek')
	else:
		print('Poza krawedzia')
elif y < 100:
	if 0 <= x < 10:
		print('Lewy Dolny')
	elif x <= 90:
		print('Prawa krawedz')
	elif x <= 100:
		print('Prawy Dolny')
	else:
		print('Poza krawedzia')
else:
	print('Poza krawedzia')


if 0 <= x < 10:
	poz_x = 'Lewy'
elif 10 < x <= 90:
	poz_x = 'Srodek'
elif x < 100:
	poz_x = 'Prawy'
else:
	poz_x = 'Y poza plansza'

if 0 <= y < 10:
	poz_y = 'Gorny'
elif 10 < y <= 90:
	poz_y = 'Srodek'
elif x < 100:
	poz_y = 'Dolny'
else:
	poz_y = 'X poza plansza'


print(f'Druga metoda: {poz_x} {poz_y}')
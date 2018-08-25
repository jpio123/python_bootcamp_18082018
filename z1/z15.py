from random import randint

ZAKRES = 10
x_gracza = randint(1, ZAKRES)
y_gracza = randint(1, ZAKRES)
x_skarbu = randint(1, ZAKRES)
y_skarbu = randint(1, ZAKRES)
nr_ruchu = 0

dyst_x = abs(x_skarbu - x_gracza)
dyst_y = abs(y_skarbu - y_gracza)
dystans = dyst_x + dyst_y

print('Let\'s play a game...')

while True:
	if ( x_gracza == x_skarbu and y_gracza == y_skarbu):
		print(f'Znalazles skarb w {nr_ruchu} ruchu, brawo!')
		break
	elif ( x_gracza < 0 or x_gracza > 10 or y_gracza < 0 or y_gracza > 10):
		print(f'Wyszedłeś z planszy, nara!')
		break
	ruch = input(f'Jestes na polu {x_gracza},{y_gracza} podaj kierunek ruchu (g d p l): ')	
	if ruch == 'l':
		x_gracza -= 1
	elif ruch == 'p':
		x_gracza += 1
	elif ruch == 'g':
		y_gracza += 1		
	elif ruch == 'd':
		y_gracza -= 1
	else:
		print('wybierz odpowiednia komende')
		continue
	dyst_x = abs(x_skarbu - x_gracza)
	dyst_y = abs(y_skarbu - y_gracza)
	nowy_dyst = dyst_x + dyst_y
	if (nowy_dyst < dystans):
		print('Bliżej')
	else:
		print('Dalej')
	dystans = nowy_dyst
	# print(f'odlegośc od skarbu: {dystans}')
		
	nr_ruchu += 1
	
	


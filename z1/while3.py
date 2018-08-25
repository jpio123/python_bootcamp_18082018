from random import randint

ZAKRES = 10

x = randint(1,ZAKRES)
y = randint(1,ZAKRES)

proba = 0

while True:
	proba += 1
	wynik = int(input(f'Podaj iloczyn liczb {x} i {y}: '))
	if wynik == x*y:
		print(f'Brawo, dobry wynik, udało Ci się za {proba} razem.')
		break
	print(f'Niestety')

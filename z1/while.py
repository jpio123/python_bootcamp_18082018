skarbonka = 20

while skarbonka < 100:
	print(f'W skarbonce jest {skarbonka} zł')
	darowizna = int(input('Kwota darowizny: '))
	skarbonka = skarbonka + darowizna

print(f'Brawo, uzbierałeś {skarbonka} :-)')
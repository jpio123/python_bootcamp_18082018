suma = 0
i = 1

while i <= 7 :
	tmp = float(input(f'Podaj sumaeraturę dnia nr {i}: '))
	suma = suma + tmp
	i += 1

srednia_suma = suma / 7
print(f'Srednia sumaetura z tygodnia to {srednia_suma} :-)')



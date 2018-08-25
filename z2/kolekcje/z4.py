
# lista = list(range(100))
# print(lista)

ile_p3 = 0
ile_p5 = 0
ile_podz = 0

for i in list(range(101)):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile_podz += 1
    if i % 3 == 0:
        ile_p3 += 1
    if i % 5 == 0:
        ile_p5 += 1
print(f'Podzielnych przez 3: {ile_p3} podzielnych przez 5: {ile_p5}, sumarycznie {ile_podz}')
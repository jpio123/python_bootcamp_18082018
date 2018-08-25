
liczby = [5, 2, -1, 4, 3]

print(liczby)

ind_max = 0
ind_min = 0
wart_max = 0
wart_min = 0

for i in(range(len(liczby))):
    if liczby[i] > liczby[ind_max]:
        ind_max = i
    elif liczby[i] < liczby[ind_min]:
        ind_min = i

print(f'Index max to: {ind_max} index min to: {ind_min}')
print("Teraz zamiana")

wart_min = liczby[ind_min]
wart_max = liczby[ind_max]

liczby[ind_min] = wart_max
liczby[ind_max] = wart_min

# liczby[ind_min], liczby[ind_max] = liczby[ind_max], liczby[ind_min]

print(liczby)
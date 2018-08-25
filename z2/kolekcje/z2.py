
liczby = []

# for i in range(10):
#     podana = int(input("Podaj liczbę: "))
#     liczby.append(podana)


while len(liczby) < 10:
    podana = input("Podaj liczbę: ")
    if podana == 'k':
        break
    else:
        liczby.append(int(podana))

print("Podałeś liczby: ",liczby)
print("Ich suma to: ", sum(liczby))
print("Ich srenia to: ", sum(liczby)/10)
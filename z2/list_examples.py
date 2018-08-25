

imiona = ["Robert", "Kamil", "Piotrek", "Karolina"]

print(type(imiona))
print(imiona)
print(len(imiona))
print("Robert" in imiona)
print("Rafal" in imiona)

for imie in imiona:
    print(imie)

for i in imiona:
    print(i)

print("Pierwsze imie to: ", imiona[0])
print("Drugie imie to: ", imiona[1])
print("Ostanie imie to: ", imiona[-1])
print("przedostanie imie to: ", imiona[-2])
print("Wybrane imiona to: ", imiona[1:3])

print(dir(imiona))

print(imiona)
imiona.append("Rafał")
print(imiona)
print(imiona.pop())
print(imiona)
imiona.remove("Kamil")
print(imiona)
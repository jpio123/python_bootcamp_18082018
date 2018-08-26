

napis = input('Podaj jakiś napis: ')

print(napis)
znaki = {}

for l in napis.lower():
    if l in znaki:
        znaki[l] += 1
    else:
        znaki[l] = 1

    # albo zamiast ifa
    # znaki[l] = znaki.get(l, 0) + 1

print(znaki)

for l in znaki:
    print(f'Litera {l} wystąpiła  {znaki[l]} razy')
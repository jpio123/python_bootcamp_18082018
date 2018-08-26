

def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True

def test_czy_pierwsza_dla_pierwszej():
    assert czy_jest_pierwsza(3)
    assert czy_jest_pierwsza(5)

def test_czy_pierwsza_dla_nie_pierwszej():
    assert not czy_jest_pierwsza(6)
    assert not czy_jest_pierwsza(4)

print(1,czy_jest_pierwsza(1))
print(2,czy_jest_pierwsza(2))
print(3, czy_jest_pierwsza(3))
print(5, czy_jest_pierwsza(5))
print(6, czy_jest_pierwsza(6))
print(7, czy_jest_pierwsza(7))
print(8, czy_jest_pierwsza(8))
print(9, czy_jest_pierwsza(9))
print(10, czy_jest_pierwsza(10))
print(11, czy_jest_pierwsza(11))
print(12, czy_jest_pierwsza(12))
print(13, czy_jest_pierwsza(13))

piepie = 0

while True:
    if czy_jest_pierwsza(piepie):
        print(piepie)
    piepie += 1
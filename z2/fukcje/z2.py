

def wiecej_niz(napis, ile):

    print(f'\nNapis: ', napis)
    print(f'Ile: ', ile)

    znaki = {}
    zbior = set()

    for l in napis.lower():
        znaki[l] = znaki.get(l, 0) + 1

    print('Znaki: ', znaki)

    for i in znaki:
        if znaki[i] > ile:
            zbior.add(i)

    print('Zbior: ', zbior)
    return zbior

def test_wiecej_niz_dla_pustego():
    assert wiecej_niz('', 1) ==  set()

def test_wiecej_niz_dla_niepustych():
    assert wiecej_niz('Ala ma kota a kot ma ale', 3) ==  {'a', ' '}
    assert wiecej_niz('Ala ma kota a kot ma ale', 6) == {'a'}
    assert wiecej_niz('aaa', 2) == {'a'}
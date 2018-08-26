
def test_formatuj_napis_bez_znacznikow():
        assert formatuj("Hello World") == 'Hello World'

def test_formatuj_wiele_napisow_bez_znacznikow():
        assert formatuj("Hello World", "I am Rafal") == 'Hello World\nI am Rafal'


def test_formatuj_wiele_napisow_ze_znacznikami():
    assert formatuj("koszt $cena PLN", "kwota $cena brutto", cena=10) == 'koszt 10 PLN\nkwota 10 brutto'

def formatuj(*napisy, **znaczniki):

    napisy = "\n".join(napisy)

    for znacznik in znaczniki:
        napisy = napisy.replace(f'${znacznik}', str(znaczniki[znacznik]))

    return napisy

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        prod = f'"{self.name}", id: {self.id}, cena: {self.price} PLN'
        print(prod)

def test_product_exist():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)

    # out, err = capsys.readouterr()
    out, _ = capsys.readouterr()

    # assert product.print_info() == '"Woda", id: 1, cena: 10.99 PLN'
    assert out == '"Woda", id: 1, cena: 10.99 PLN'
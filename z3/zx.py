
class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        prod = f'"{self.name}", id: {self.id}, cena: {self.price} PLN'
        print(prod)

class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Basket:

    def __init__(self):

        self.entries = []

    def add_product(self, product, count):



    def count_total_price(self):
        pass

    def generate_report(self):
        pass


def test_basket(capsys):
    basket = Basket()
    assert basket.entries == []
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    basket.add_product(product, 5)

    assert len(basket.entries) == 1
    assert basket.count_total_price() == 50
    basket.generate_report()
    out, _ = capsys.readouterr()
    assert out == 'Produkty w koszyku:\n - Woda(1), cena: 10.00 x 5\n W sumie: 50.00'
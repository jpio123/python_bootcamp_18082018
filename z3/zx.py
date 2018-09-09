class Product:

    def __init__(self, id, name, price):
        self.price = price

        self._id = id
        self._name = name
        self._discount = 0

    def print_info(self):
        prod = f'"{self._name}", id: {self._id}, cena: {self.price} PLN, znizka: {self._discount}%'
        print(prod)

    @property
    def full_name(self):
        return 'Product: ' + self._name

    @property
    def discount_value(self):
        return self.price * self._discount / 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self.name = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if type(discount) == int and 0 <= discount <= 30:
            self._discount = discount


def test_discount():
    product = Product(1, 'Woda', 10.00)
    product.print_info()
    product.discount = 30
    assert product.discount == 30
    assert product.discount_value == 3
    product.discount = 40
    assert product.discount == 30
    assert product.discount_value == 3
    product.print_info()

# class BasketEntry:
#
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity
#
# class Basket:
#
#     def __init__(self):
#
#         self.entries = []
#
#     def add_product(self, product, count):
#
#
#
#     def count_total_price(self):
#         pass
#
#     def generate_report(self):
#         pass
#
#
# def test_basket(capsys):
#     basket = Basket()
#     assert basket.entries == []
#     product = Product(1, 'Woda', 10.00)
#     basket.add_product(product, 5)
#     basket.add_product(product, 5)
#
#     assert len(basket.entries) == 1
#     assert basket.count_total_price() == 50
#     basket.generate_report()
#     out, _ = capsys.readouterr()
#     assert out == 'Produkty w koszyku:\n - Woda(1), cena: 10.00 x 5\n W sumie: 50.00'

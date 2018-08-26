

lista = [x / 10 for x in range(11)]
print(lista)

tuple3 = [(x, x**2, x**3) for x in range(-10,11)]
print(tuple3)

napisy = {'123', '12345', '123456789', '1234567'}

dlugosci = {x: len(x) for x in napisy}
print(dlugosci)
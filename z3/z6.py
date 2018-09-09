import math

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        v_ret = Vector(self.x + other.x, self.y + other.y)
        return v_ret

    def __sub__(self, other):
        v_ret = Vector(self.x - other.x, self.y - other.y)
        return v_ret

    def __mul__(self, other):
        v_ret = Vector(self.x * other, self.y * other)
        return v_ret

    @property
    def lenght(self):
        len = math.sqrt(self.x ** 2 + self.y ** 2)
        return len

    def __eq__(self, other):
        return self.lenght == other.lenght

    def __gt__(self, other):
        return self.lenght > other.lenght

    def __ge__(self, other):
        return self.lenght >= other.lenght

    def __lt__(self, other):
        return self.lenght < other.lenght

    def __le__(self, other):
        return self.lenght <= other.lenght

    def __ne__(self, other):
        return self.lenght != other.lenght

    def __str__(self):
        return f'V{self.x},{self.y}    {self.lenght}'


def test_vector_create():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    assert v1.x == 1
    assert v1.y == 2


def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_vector_sub():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 - v2
    assert v3.x == -2
    assert v3.y == -2


def test_vector_mult():
    v1 = Vector(1, 2)
    mult = 3
    v3 = v1 * mult
    assert v3.x == 3
    assert v3.y == 6


def test_vector_len():
    v1 = Vector(3, 4)

    assert v1.lenght == 5


def test_vectors_equal():
    v1 = Vector(3, 4)
    v2 = Vector(-3, 4)
    assert v1 == v2


def test_vectors_equal2():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    assert v1 == v2


def test_vectors_equal3():
    v1 = Vector(3, 4)
    v2 = Vector(0, 5)
    assert v1 == v2


def test_greater_than():
    v1 = Vector(3, 5)
    v2 = Vector(3, 4)

    assert v1 > v2
    assert not v2 > v1


def test_all_operators():
    v1 = Vector(3, 5)
    v2 = Vector(3, 4)
    v3 = Vector(3, 4)

    assert v1 > v2
    assert v1 >= v2
    assert v2 >= v3

    assert not v1 <= v2
    assert v2 <= v3
    assert not v1 < v2
    assert v2 < v1

    assert v1 != v2

def test_sort():
    v1 = Vector(3, 5)
    v2 = Vector(0, 4)
    v3 = Vector(0, 10)

    lista = [v1, v2, v3]
    assert sorted(lista) == [v2, v1, v3]

    print("\nUnsorted:")
    for v in lista:
        print(v)

    lista = sorted(lista)
    print("\nSorted:")
    for v in lista:
        print(v)


# def test_vector_add_non_vector():
#     v1 = Vector(1, 2)
#     v2 = v1 + 4


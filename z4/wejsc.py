import pytest


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "knock knock"

    def __gt__(self, other):
        return self.age > other.age

class Dog(Animal):

    def sound(self):
        return "how how"


class Cat(Animal):
    pass

    def sound(self):
        return "... (sorry - that's cat!)"

def test_animal():
    animal = Animal("Strange something", 1000)
    assert animal.name == "Strange something"
    assert animal.age == 1000
    assert animal.sound() == "knock knock"


def test_cat_dog():
    animal = Animal("Strange something", 1000)
    cat = Cat("Albert", 5)
    dog = Dog("Ninja", 6)
    assert dog.sound() == "how how"
    assert cat.sound() == "... (sorry - that's cat!)"

    assert dog > cat
    assert not dog > animal

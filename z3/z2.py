import pytest

class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.time = 0
        self.nadg = 0

    def register_time(self, time):
        self.time += time

    def pay_salary(self):

        if self.time <=8:
            salary = self.time * self.stawka
        else:
            salary = 8 * self.stawka + (self.time-8) * self.stawka * 2

        self.time = 0

        return salary

    def register_time_2(self, time):

        if time <= 8:
            self.time += time
        else:
            self.time = 8
            self.nadg = time - 8


    def pay_salary_2(self):

        podstawa = self.time * self.stawka
        nadgodziny = self.nadg * self.stawka * 2

        self.time = 0
        self.nadg = 0

        return podstawa + nadgodziny


def test_register():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0
    employee.register_time(10)
    assert employee.pay_salary() == 1200

def test_register_2():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time_2(5)
    employee.register_time_2(5)
    assert employee.pay_salary_2() == 1000
    assert employee.pay_salary_2() == 0
    employee.register_time_2(10)
    employee.register_time_2(5)
    assert employee.pay_salary_2() == 1700
    assert employee.pay_salary_2() == 0
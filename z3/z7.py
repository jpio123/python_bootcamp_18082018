import pytest

class Employee:
   def __init__(self, name, lastname, wage):
       self.name = name
       self.lastname = lastname
       self.wage = wage
       self.registered_time = 0

   def register_time(self, hours):
       if hours > 24:
           raise ValueError
       self.registered_time += hours

   def pay_salary(self):
       if self.registered_time <= 8:
           payment = self.registered_time * self.wage
       else:
           normal_hours = 8
           overhours = self.registered_time - 8
           payment = normal_hours * self.wage + overhours * self.wage * 2
       self.registered_time = 0
       return payment


class PremiumEmployee(Employee):
    def __init__(self, name, lastname, wage, bonus=0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    pass

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary()  # super().pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal

def test_create():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 0

def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonus(1000)
    emp.give_bonus(400)
    assert emp.pay_salary() == 1900

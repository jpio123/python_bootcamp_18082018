
class ElectricCar:
    def __init__(self, maxrange):
        self.maxrange = maxrange
        self.range = maxrange

    def drive(self, distance):

        if distance <= self.range:
            self.range = self.range - distance
            return distance
        else:
            drove =  self.range
            self.range = 0
            return drove
    def charge(self):
            self.range = self.maxrange

def test_electric_car():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50


def test_electric_car_2():
    car = ElectricCar(120)
    assert car.drive(70) == 70
    assert car.drive(50) == 50
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50

class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.start_engine = True
        print("You can turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward.")

    def turn_left(self):
        self.fuel -= 1
        print("The Car turns left.")

    def turn_off(self):
        self.engine_status = False
        print("The car is off.")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


class KeylessCar():
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name, milage)

    def start_engine(self):
        self.engine_status = True
        print("You push ")
jacob_car = Impala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_left()






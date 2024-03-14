class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Двигун запущено")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print("Двигун автомобіля запущено")


class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def start_engine(self):
        print("Двигун мотоцикла запущено")


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def charge_battery(self):
        print("Батарея заряджається")

    def start_engine(self):
        print("Двигун електромобіля запущено")


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)

    def start_all_engines(self):
        for vehicle in self.vehicles:
            vehicle.start_engine()


car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Harley-Davidson", "Cruiser")
electric_car = ElectricCar("Tesla", "Model S")

garage = Garage()
garage.add_vehicle(car)
garage.add_vehicle(motorcycle)
garage.add_vehicle(electric_car)

garage.start_all_engines()

electric_car.charge_battery()

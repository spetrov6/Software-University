from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel_amount):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 0.9
        needed_fuel_amount = self.fuel_consumption * distance
        if self.fuel_quantity > needed_fuel_amount:
            self.fuel_quantity -= needed_fuel_amount

    def refuel(self, fuel_amount):
        self.fuel_quantity += fuel_amount


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 1.6
        needed_fuel_amount = self.fuel_consumption * distance
        if self.fuel_quantity >= needed_fuel_amount:
            self.fuel_quantity -= needed_fuel_amount

    def refuel(self, fuel_amount):
        self.fuel_quantity += fuel_amount * 0.95

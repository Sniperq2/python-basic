from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 100, fuel: int = 9, fuel_consumption: int = 1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        expected = self.fuel - distance * self.fuel_consumption
        if expected >= 0:
            self.fuel = expected
        else:
            raise NotEnoughFuel

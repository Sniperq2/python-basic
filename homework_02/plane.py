"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0
        self.prev_cargo = 0

    def load_cargo(self, additional_cargo: int) -> None:
        self.prev_cargo = self.cargo
        new_cargo = self.cargo + additional_cargo
        if self.max_cargo >= new_cargo:
            self.prev_cargo = self.cargo
            self.cargo = new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> int:
        self.cargo = 0
        return self.prev_cargo

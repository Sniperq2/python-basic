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

    def load_cargo(self, additional_cargo: int) -> None:
        if self.max_cargo >= self.cargo + additional_cargo:
            self.cargo += additional_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> int:
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo

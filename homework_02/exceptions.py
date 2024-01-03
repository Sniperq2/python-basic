"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self):
        pass


class NotEnoughFuel(Exception):
    def __init__(self):
        pass


class CargoOverload(Exception):
    def __init__(self):
        pass

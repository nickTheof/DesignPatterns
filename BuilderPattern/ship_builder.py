from interface_ship_builder import IShipBuilder
from ship import Ship


class ShipBuilder(IShipBuilder):
    "The Ship Builder"

    def __init__(self) -> None:
        self.ship = Ship()

    def set_ship_type(self, type):
        self.ship.type = type
        return self

    def set_ship_flag(self, flag):
        self.ship.flag = flag
        return self

    def set_length(self, length):
        self.ship.length = length
        return self

    def set_tonnage(self, tonnage):
        self.ship.tonnage = tonnage
        return self

    def set_capacity(self, capacity):
        self.ship.capacity = capacity
        return self

    def get_result(self):
        return self.ship

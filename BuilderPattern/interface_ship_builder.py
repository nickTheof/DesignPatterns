from abc import ABC, abstractmethod


class IShipBuilder(ABC):
    "The Ship Builder Interface"

    @staticmethod
    @abstractmethod
    def set_ship_type(type):
        "Ship type"

    @staticmethod
    @abstractmethod
    def set_ship_flag(flag):
        "Ship flag"

    @staticmethod
    @abstractmethod
    def set_length(length):
        "Length of ship"

    @staticmethod
    @abstractmethod
    def set_tonnage(tonnage):
        "Tonnage of Ship"

    @staticmethod
    @abstractmethod
    def set_capacity(capacity):
        "Capacity of Ship"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

"The Abstract Factory Interface"

from abc import ABC, abstractmethod


class ICarEquipmentFactory(ABC):
    "Abstract Car's Equipment Factory Interface"

    @staticmethod
    @abstractmethod
    def get_equipment(equipment):
        "The static Abstract factory interface method"

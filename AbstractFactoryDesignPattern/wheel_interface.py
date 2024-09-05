from abc import ABC, abstractmethod


class Wheel(ABC):
    "The Wheel abstract interface"

    @staticmethod
    @abstractmethod
    def get_infos():
        "A static interface method"

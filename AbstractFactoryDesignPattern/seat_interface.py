from abc import ABC, abstractmethod


class Seat(ABC):
    "The Seat abstract interface"

    @staticmethod
    @abstractmethod
    def get_infos():
        "A static interface method"
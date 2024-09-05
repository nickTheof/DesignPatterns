from abc import ABC, abstractmethod


class Person(ABC):
    "The interface of a Person Object"

    @staticmethod
    @abstractmethod
    def get_info():
        "A static interface method"



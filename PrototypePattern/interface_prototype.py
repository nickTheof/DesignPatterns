from abc import ABC, abstractmethod


class IPrototype(ABC):
    "The Prototype Interface with clone method"

    @staticmethod
    @abstractmethod
    def clone(mode):
        "The clone, deep or shallow."

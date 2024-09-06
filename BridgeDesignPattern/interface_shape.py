from abc import ABC, abstractmethod


class IShape(ABC):
    "A shape Interface"

    @staticmethod
    @abstractmethod
    def draw():
        """Will be handled by the shapes implementer"""
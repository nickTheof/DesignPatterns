from abc import ABC, abstractmethod


class IShapeImplementer(ABC):
    "A shape Interface"

    @staticmethod
    @abstractmethod
    def draw_implementation():
        """The method that the refined abstractions will implement"""
        
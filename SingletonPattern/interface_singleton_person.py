from abc import ABC, abstractmethod


class IPerson(ABC):

    @staticmethod
    @abstractmethod
    def print_data():
        """implement in child class"""

from abc import ABC, abstractmethod


class IDepartment(ABC):

    @abstractmethod
    def __init__(self, employees):
        """Implement in child class"""

    @staticmethod
    @abstractmethod
    def print_department():
        """Implement in child class"""


class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees} employees")


class Devs(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Developers Department: {self.employees} employees")


class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.deps = []

    def add(self, dept: IDepartment):
        self.deps.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for department in self.deps:
            department.print_department()
        print(f"Total number of employees: {self.employees}")

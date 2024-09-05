from interface_person import Person


class Teacher(Person):
    "The Teacher Concrete Class implements the Person interface"

    def __init__(self, age: int, first_name: str, last_name: str, course: str) -> None:
        self._age = age
        self._first_name = first_name
        self._last_name = last_name
        self._course = course

    def get_info(self) -> dict:
        return {
            "age": self._age,
            "full name": f"{self._first_name} {self._last_name}",
            "course": self._course,
        }

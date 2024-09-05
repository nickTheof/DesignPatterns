from athele_person import Athlete
from doctor_person import Doctor
from teacher_person import Teacher


class PersonFactory:
    "The Factory Class"

    @staticmethod
    def create_person(person):
        "A static method tries to get infos of a person object"
        try:
            if person == "athlete":
                return Athlete(35, "Nickolas", "Rambo", "Crossfit")
            elif person == "doctor":
                return Doctor(45, "John", "Stockton", "Neuro")
            elif person == "teacher":
                return Teacher(25, "Natalia", "Williams", "Maths")
            else:
                raise Exception("Person doesnt found")
        except Exception as _e:
            print(_e)
        return None

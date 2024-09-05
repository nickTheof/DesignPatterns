from seat_interface import Seat


class MediumSeat(Seat):

    "The  Medium Seat Concrete Class implements the Seat interface"

    def __init__(self):
        self._height = 65
        self._width = 20
        self._length = 65

    def get_infos(self):
        return {"width": self._width, "depth": self._length, "height": self._height}

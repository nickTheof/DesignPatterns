from seat_interface import Seat


class BigSeat(Seat):

    "The Big Seat Concrete Class implements the Seat interface"

    def __init__(self):
        self._height = 75
        self._width = 22
        self._length = 65

    def get_infos(self):
        return {"width": self._width, "depth": self._length, "height": self._height}

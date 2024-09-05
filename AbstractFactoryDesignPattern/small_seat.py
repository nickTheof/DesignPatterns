from seat_interface import Seat

class SmallSeat(Seat):

    "The Small Seat Concrete Class implements the Seat interface"

    def __init__(self):
        self._height = 60
        self._width = 15
        self._length = 60

    def get_infos(self):
        return {
            "width": self._width,
            "depth": self._length,
            "height": self._height
        }
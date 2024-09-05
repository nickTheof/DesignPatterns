from small_seat import SmallSeat
from medium_seat import MediumSeat
from big_seat import BigSeat

class SeatFactory:  
    "The Factory Class"

    @staticmethod
    def get_seat(seat):
        "A static method to get a seat"
        try:
            if seat == 'smallSeat':
                return SmallSeat()
            if seat == 'mediumSeat':
                return MediumSeat()
            if seat == 'bigSeat':
                return BigSeat()
            raise Exception('seat Not Found')
        except Exception as _e:
            print(_e)
        return None
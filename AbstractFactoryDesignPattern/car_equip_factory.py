from car_equip_factory_interface import ICarEquipmentFactory
from wheel_factory import WheelFactory
from seat_factory import SeatFactory


class CarEquipmentFactory(ICarEquipmentFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_equipment(equipmnent):
        "Static get_factory method"
        try:
            if equipmnent in ['RubberWheel', 'NylonWheel', 'PUWheel']:
                return WheelFactory.get_wheel(equipmnent)
            if equipmnent in ['smallSeat', 'mediumSeat', 'bigSeat']:
                return SeatFactory.get_seat(equipmnent)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
from rubber_wheel import RubberWheel
from nylon_wheel import NylonWheel
from pu_wheel import PuWheel

class WheelFactory:  
    "The Factory Class"

    @staticmethod
    def get_wheel(wheel):
        "A static method to get a wheel"
        try:
            if wheel == 'RubberWheel':
                return RubberWheel()
            if wheel == 'NylonWheel':
                return NylonWheel()
            if wheel == 'PUWheel':
                return PuWheel()
            raise Exception('Wheel Not Found')
        except Exception as _e:
            print(_e)
        return None

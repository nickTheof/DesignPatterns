from wheel_interface import Wheel

class NylonWheel(Wheel):

    def __init__(self) -> None:
        self._elasticity = "not acceptable"
        self._weather_resistance = "excellent"
        self._heat_resistance = 70


    def get_infos(self):
        return {
            "elasticity": self._elasticity,
            "weather resistance": self._weather_resistance,
            "heat resistance": self._heat_resistance
        }        
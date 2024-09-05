"A Director Class"
from ship_builder import ShipBuilder


class PassengerDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return (
            ShipBuilder()
            .set_ship_type("Passenger")
            .set_ship_flag("IT")
            .set_length(150)
            .set_tonnage(5000)
            .set_capacity(350)
            .get_result()
        )

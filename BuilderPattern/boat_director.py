"A Director Class"
from ship_builder import ShipBuilder


class BoatDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return (
            ShipBuilder()
            .set_ship_type("boat")
            .set_ship_flag("Greece")
            .set_length(6)
            .set_tonnage(5)
            .set_capacity(8)
            .get_result()
        )

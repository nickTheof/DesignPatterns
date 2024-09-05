"A Director Class"
from ship_builder import ShipBuilder


class TankerDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return (
            ShipBuilder()
            .set_ship_type("Tanker")
            .set_ship_flag("USA")
            .set_length(200)
            .set_tonnage(15000)
            .set_capacity(50)
            .get_result()
        )

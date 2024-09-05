class Ship:
    "The Ship"

    def __init__(
        self,
        type: str = "Container",
        flag: str = "GR",
        length: int = 200,
        tonnage: int = 10000,
        capacity: int = 40,
    ) -> None:
        self.type = type
        self.flag = flag
        self.length = length
        self.tonnage = tonnage
        self.capacity = capacity

    def construction(self):
        return (
            f"Boat Information:\n"
            f"Type: {self.type}\n"
            f"Flag: {self.flag}\n"
            f"Length: {self.length} meters\n"
            f"Tonnage: {self.tonnage} tons\n"
            f"Capacity: {self.capacity} passengers"
        )

class SmartPhone:

    def __init__(self, properties) -> None:
        self.__properties = properties

    def sell(self, owner: str, price: int):
        common = self.__properties

        print(f"Smartphone {common} is sold to {owner} for price {price}.")

    def __repr__(self) -> str:
        return f"Smarthone (properties={self.__properties})"


class SmartPhoneFactory:

    __smartphones: dict[str, SmartPhone] = {}

    def get_smartphone(self, properties: list[str]) -> SmartPhone:
        key = "-".join(properties)
        if key in self.__smartphones:
            print(f"Returning already existing smartphone object for {properties}")
        else:
            print(f"New smartphone object created for {properties}")
            self.__smartphones.update({key: SmartPhone(properties)})
        return self.__smartphones[key]

    def list_smartphones(self) -> list[SmartPhone]:
        smartphones = self.__smartphones.values()

        for phone in smartphones:
            print(phone)

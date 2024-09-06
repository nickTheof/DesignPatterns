from lightweight import SmartPhone, SmartPhoneFactory

factory = SmartPhoneFactory()

smartphone = factory.get_smartphone(["Samsung", "Galaxy S24", "Black", "256GB"])
smartphone.sell("Nickolas", 750)

smartphone = factory.get_smartphone(["Samsung", "Galaxy S23", "White", "128GB"])
smartphone.sell("John", 500)

smartphone = factory.get_smartphone(["Samsung", "Galaxy S24", "Black", "256GB"])
smartphone.sell("Harry", 790)

factory.list_smartphones()

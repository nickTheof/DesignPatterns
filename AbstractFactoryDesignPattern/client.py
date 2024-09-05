
"Abstract Factory Use Case Example Code"

from car_equip_factory import CarEquipmentFactory

EQUIPMENT = CarEquipmentFactory.get_equipment("RubberWheel")
print(f"{EQUIPMENT.__class__} : {EQUIPMENT.get_infos()}")

EQUIPMENT = CarEquipmentFactory.get_equipment("bigSeat")
print(f"{EQUIPMENT.__class__} : {EQUIPMENT.get_infos()}")

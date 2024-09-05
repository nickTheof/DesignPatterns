"Ship Builder Example Code"

from boat_director import BoatDirector
from passenger_director import PassengerDirector
from tanker_director import TankerDirector

BOAT = BoatDirector.construct()
PASSENGER_SHIP = PassengerDirector.construct()
TANKER = TankerDirector.construct()


print(BOAT.construction())
print(PASSENGER_SHIP.construction())
print(TANKER.construction())

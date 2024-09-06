from circle_implementer import CircleImplementer
from circle import Circle
from square_implementer import SquareImplementer
from square import Square


CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()


SQUARE = Square(SquareImplementer)
SQUARE.draw()

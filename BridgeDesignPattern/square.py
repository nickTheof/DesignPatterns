from interface_shape import IShape


class Square(IShape):

    def __init__(self, implementer) -> None:
        self.implementer = implementer

    def draw(self) -> None:
        self.implementer.draw_implementation()

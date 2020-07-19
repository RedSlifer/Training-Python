import math
from Geometric import Geometric


class Circle(Geometric):    # Circle class inherits Geometric class
    def __init__(self, radius=1):
        super().__init__()  # Calls the superclass constructor
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius < 0:
            raise RuntimeError('Negative radius')
        else:
            self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_diameter(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return super().__str__() + ' radius: ' + str(self.__radius)

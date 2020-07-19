from Geometric import Geometric


class Rectangle(Geometric):
    def __init__(self, width=1, height=1):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return super().__str__() + ' width: ' + str(self.__width) + ' height: ' + str(self.__height)

from Rectangle import Rectangle
from Circle import Circle


def main():
    try:
        circle = Circle()
        circle.set_radius(-1)   # Invalid value for radius
        print('A circle', circle)
        print('The radius is', circle.get_radius())
        print('The area is', circle.get_area())
        print('The diameter is', circle.get_diameter())

    except RuntimeError as exception:
        print(exception)


def display_object(geometric_object):
    print('Area is', geometric_object.get_area())
    print('Perimeter is', geometric_object.get_perimeter())

    if isinstance(geometric_object, Rectangle):
        print('Width is', geometric_object.get_width())
        print('Height is', geometric_object.get_height())
    elif isinstance(geometric_object, Circle):
        print('Diameter is', geometric_object.get_diameter())


def is_same_area(geometric_object_1, geometric_object_2):
    return geometric_object_1.get_area() == geometric_object_2.get_area()


main()

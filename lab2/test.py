import unittest

from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle


green = "зелёного"
red = "красного"
yellow = "жёлтого"


class TestFigures(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(2, 4, red)
        self.b = Circle(4, yellow)
        self.c = Square(4, green)

    def test_area(self):
        from math import pi
        self.assertEqual(self.a.area(), 8)
        self.assertEqual(self.b.area(), pi * 4 * 4)
        self.assertEqual(self.c.area(), 16)

    def test_color(self):
        self.assertEqual(self.a.r_color._color, red)
        self.assertEqual(self.b.c_color._color, yellow)
        self.assertEqual(self.c.r_color._color, green)

    def test_repr(self):
        self.assertEqual(str(self.a), 'Прямоугольник красного цвета с длиной 4, шириной 2, площадью 8.')
        self.assertEqual(str(self.b), 'Круг жёлтого цвета радиусом 4, площадью 50.26548245743669.')
        self.assertEqual(str(self.c), 'Квадрат зелёного цвета с длиной стороны 4, площадью 16.')


def main():
    print(Rectangle(2, 4, red))
    print(Circle(4, yellow))
    print(Square(4, green))


if __name__ == "__main__":
    main()










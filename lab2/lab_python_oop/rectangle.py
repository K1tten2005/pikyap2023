from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    type = "Прямоугольник"

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.r_color = Color(color)

    def area(self):
        return self.width * self.length

    def __repr__(self):
        return '{} {} цвета с длиной {}, шириной {}, площадью {}.'.format(
            self.type,
            self.r_color._color,
            self.length,
            self.width,
            self.area()
        )
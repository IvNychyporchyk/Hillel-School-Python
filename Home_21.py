# Создать класс Circle на базе класса Point
# Класс должен поддерживать все методы родительского класса, а так же:
# минимальное расстояние от окружности до центра координат;
# площадь окружности и длину окружности.

# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math


class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        if self.radius == other.radius:
            return Point()
        # else:
        #     return Circle(f"Circle: {self.radius}, {self.x}, {self.y}")

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == '__main__':
    circle_1 = Circle(7, 1, 1)
    print("-" * 50)
    print(circle_1.circumference())
    print("-" * 50)
    print(circle_1)
    circle_2 = Circle(7, 1, 4)
    print("-" * 50)
    print(circle_2.distance_from_origin())
    print("-" * 50)
    print(circle_2)

    circle_3 = circle_1 + circle_2
    print(circle_3)
    print(circle_3.area())
    print("-" * 50)
    circle_4 = circle_1 == circle_2
    print("eq", circle_4)
    print("-" * 50)
    circle_5 = circle_1 - circle_2
    print(circle_5)
    print("-" * 50)

# 3) Точка на карте (свойства: X, Y).
# Методы:
# 1. Нужно вычислить расстояние до начала координат,
# 2. * вычисляется расстояние между точкой и другой точкой экземпляром этого же
# класса
# 3. ** перевод в другие системы координат
from math import sqrt


class Point:
    """Constructs all the necessary attributes for the Point object"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Print the object"""
        return f"X-coordinate: {self.x}, Y-coordinate: {self.y}"

    def distance_to_zero(self):
        """Returns the distance to the point with (0, 0) coordinates"""
        return sqrt(self.x**2 + self.y**2)


def distance_to_point(point1, point2):
    """Accepts two points and returns the distance between them"""
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


p1 = Point(1, 4)
p2 = Point(4, 1)
print(p1.__str__())
print(p1.distance_to_zero())
print(distance_to_point(p1, p2))



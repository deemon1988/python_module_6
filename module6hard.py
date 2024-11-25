# Дополнительное практическое задание по модулю: "Наследование классов."

import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.initialize_sides(sides)
        self.__color = list(color)
        self.filed = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        is_valid = True
        for i in [r, g, b]:
            if i not in range(0, 256) and not isinstance(i, int):
                is_valid = False
        return is_valid

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        is_valid = True
        for side in list(*sides):
            if side < 0 or not isinstance(side, int):
                is_valid = False
        return len(sides) == self.sides_count and is_valid

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def initialize_sides(self, *sides):
        if len(sides) > 1 and len(sides) != self.sides_count:
            return [1] * self.sides_count
        else:
            return list(*sides) * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_radius(sides)

    def get_radius(self, sides):
        return sum(self.initialize_sides(sides)) / (2 * math.pi)

    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
            self.__radius = self.get_radius(new_sides)

    def get_sides(self):
        return self.__sides

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum((a, b, c)) / 2
        sq = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return sq


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        if len(self.get_sides()) != 0:
            return self.get_sides()[0] ** 3


if __name__ == '__main__':
    triangle1 = Triangle((300, 200, 100), 10)
    print(triangle1.get_sides())
    print(triangle1.get_square())

    circle1 = Circle((200, 200, 100), 10)
    print(circle1._Circle__radius)
    print(circle1.get_square())
    circle1.set_sides(15)
    print(circle1._Circle__radius)
    print(circle1.get_square())
    print(circle1.get_color())
    circle1.set_color(55, 255, 77)
    print(circle1.get_color())
    circle1.set_sides(15)
    print(circle1.get_sides())
    print(len(circle1))
    print(circle1.get_square())

    cube1 = Cube((222, 35, 130), 6)
    cube1.set_color(150.1, 70, 15)  # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    # Проверка объёма (куба):
    print(cube1.get_volume())

    print(sum(circle1._Figure__sides))

    print(circle1.get_sides())
    circle1.set_sides(15)
    print(circle1._Circle__radius)
    circle1.set_sides(10)
    print(circle1._Circle__radius)
    print(circle1.get_sides())

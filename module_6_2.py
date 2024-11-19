# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств"


class Vehicle:
    __COLOR_VARIANTS = 'red', 'blue', 'green', 'orange', 'black', 'white', 'brown'

    def __init__(self, owner, __model, color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.upper() in [clr.upper() for clr in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()

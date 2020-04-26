# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг/м2/см*5см = 12500 т


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self, spec_mass, thickness):
        mass = self._length * self._width * spec_mass * thickness
        print(f'Масса асфальта составляет: {self._length} м * {self._width} м * {spec_mass} кг/м2/см * {thickness}см '
              f'= {mass} кг = {mass / 1000} т\n')


r = Road(5000, 20)
r.mass_count(25, 5)

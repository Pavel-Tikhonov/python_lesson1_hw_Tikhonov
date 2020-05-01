# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class ClothesTypeAbstract(ABC):
    @property
    @abstractmethod
    def fabric_consump(self) -> float:
        pass


class Clothes:
    def __init__(self, name: str):
        self.name = name


class Coat(Clothes, ClothesTypeAbstract):
    def __init__(self, name, size: int):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consump(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes, ClothesTypeAbstract):
    def __init__(self, name, size: int):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consump(self):
        return 2 * self.size + 0.3


c = Coat('Пальтишко', 48)
c_consump = c.fabric_consump
print(f'Расход ткани на пальто с названием "{c.name}" размера {c.size}: {c_consump:.3f}')
s = Suit('Костюмчик', 180)
s_consump = s.fabric_consump
print(f'Расход ткани на костюм с названием "{s.name}" на рост {s.size}: {s_consump:.3f}')
sum_consump = c_consump + s_consump
print(f'Общий расход ткани составляет: {sum_consump:.3f}')

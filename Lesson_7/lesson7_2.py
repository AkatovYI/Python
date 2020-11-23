# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 36:
            self.__v = 36
        elif v > 62:
            self.__v = 62
        else:
            self.__v = v

    @property
    def consumption(self):
        return f'При размере {self.v} расход ткани на пальто {self.v / 6.5 + 0.5: .2f} м'


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 100:
            self.__h = 100
        elif h > 200:
            self.__h = 200
        else:
            self.__h = h

    @property
    def consumption(self):
        return f'При росте {self.h} расход ткани на костюм {(self.h / 100) * 2 + 0.3: .2f} м'


coat = Coat(42)
print(coat.consumption)
costume = Costume(180)
print(costume.consumption)
coat = Coat(32)
print(coat.consumption)
costume = Costume(220)
print(costume.consumption)

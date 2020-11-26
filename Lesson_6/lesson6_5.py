# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery():
    title = 'Канцелярская принадлежность'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Рисуем {self.title}')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Рисуем {self.title}')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Рисуем {self.title}')

s = Stationery()
s.draw()

s = Pen()
s.draw()

s = Pencil()
s.draw()

s = Handle()
s.draw()

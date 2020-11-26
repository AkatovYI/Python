# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поехала на{direction}')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'Скорость машины превышает 60 км - {self.speed}') if self.speed > 60 else \
            print(f'Скорость машины {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        print(f'Скорость машины превышает 40 км - {self.speed}') if self.speed > 40 else \
            print(f'Скорость машины {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


t = TownCar(60, 'Зеленый', 'TownCar')
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('право')
t.stop()
print('')

t = WorkCar(40, 'Синий', 'WorkCar')
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('лево')
t.stop()
print('')

t = SportCar(240, 'Красный', 'SportCar')
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('зад')
t.stop()
print('')

t = PoliceCar(150, 'Белый', 'PoliceCar', True)
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('право')
t.stop()
print('')

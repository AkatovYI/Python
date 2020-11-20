# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self):
        self.speed = 0
        self.color = ''
        self.name = ''
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поехала на{direction}')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 60
        self.color = 'Зеленый'
        self.name = 'TownCar'

    def show_speed(self):
        print(f'Скорость машины превышает 60 км - {self.speed}') if self.speed > 60 else \
            print(f'Скорость машины {self.speed}')


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 40
        self.color = 'Синий'
        self.name = 'WorkCar'

    def show_speed(self):
        print(f'Скорость машины превышает 40 км - {self.speed}') if self.speed > 40 else \
            print(f'Скорость машины {self.speed}')


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 200
        self.color = 'Красный'
        self.name = 'SportCar'


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.color = 'Белый'
        self.name = 'PoliceCar'
        self.is_police = True


t = TownCar()
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('право')
t.stop()
print('')

t = WorkCar()
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('лево')
t.stop()
print('')

t = SportCar()
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('зад')
t.stop()
print('')

t = PoliceCar()
print(f'Имя машины: {t.name}, цвет машины: {t.color}, машина является полицейской: ', 'Да' if t.is_police else 'Нет')
print(f'Максимально разрешённая скорость для машины: {t.speed}')
t.speed = 80
print(f'Заданная скорость для машины: {t.speed}')
t.go()
t.show_speed()
t.turn('право')
t.stop()
print('')

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep
from graphics import *


class TrafficLight:
    def __init__(self):
        self.__color1 = 'red'
        self.__color2 = 'yellow'
        self.__color3 = 'green'
        self.__color4 = 'white'

    def running(self):
        obj1 = Circle(Point(200, 80), 50)
        obj2 = Circle(Point(200, 190), 50)
        obj3 = Circle(Point(200, 300), 50)
        i = 0
        while i < 3:
            obj1.setFill(self.__color1)
            obj1.draw(win)
            obj2.setFill(self.__color4)
            obj2.draw(win)
            obj3.setFill(self.__color4)
            obj3.draw(win)
            sleep(7)
            obj1.undraw()
            obj2.undraw()
            obj3.undraw()
            obj1.setFill(self.__color4)
            obj1.draw(win)
            obj2.setFill(self.__color2)
            obj2.draw(win)
            obj3.setFill(self.__color4)
            obj3.draw(win)
            sleep(2)
            obj1.undraw()
            obj2.undraw()
            obj3.undraw()
            obj1.setFill(self.__color4)
            obj1.draw(win)
            obj2.setFill(self.__color4)
            obj2.draw(win)
            obj3.setFill(self.__color3)
            obj3.draw(win)
            sleep(7)
            obj1.undraw()
            obj2.undraw()
            obj3.undraw()
            obj1.setFill(self.__color4)
            obj1.draw(win)
            obj2.setFill(self.__color2)
            obj2.draw(win)
            obj3.setFill(self.__color4)
            obj3.draw(win)
            sleep(2)
            obj1.undraw()
            obj2.undraw()
            obj3.undraw()
            i += 1


win = GraphWin("Окно для графики", 400, 400)

s = TrafficLight()
s.running()
win.close()

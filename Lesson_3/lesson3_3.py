# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    """
    Функция суммирования двух наибольших значений
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    x = arg1 + arg2 + arg3 - min(arg1, arg2, arg3)
    return x


arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))
arg3 = int(input('Введите третье число: '))

print(my_func(arg1, arg2, arg3))

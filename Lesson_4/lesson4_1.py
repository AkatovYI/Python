#1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

skript_name, product, rate, prize = argv
try:
    zarp = float(product) * float(rate) + float(prize)
    print(f'Расчет заработной платы: {round(zarp, 2)}')
except:
    print('Не верные аргументы')
#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

profit = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
if profit >= costs:
    print(f'У вас прибыль: {profit - costs}')
    print(f'Рентабильность: {(profit - costs) / profit}')
    kol = int(input('Введите численность сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {(profit - costs) / kol}')
else:
    print(f'У вас убытки: {costs - profit}')

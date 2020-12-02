#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

devid1, devid2 = input('Введите делимое и делитель через пробел: ').split()

try:
    devid1, devid2 = int(devid1), int(devid2)
    if devid1 == 0:
        raise MyOwnError('Делимое рано 0')
    elif devid2 == 0:
        raise MyOwnError('Делитель не может быть равным 0')
except (ValueError, MyOwnError) as err:
    print(err)
else:
    print(f'{devid1} / {devid2} = {devid1 / devid2}')

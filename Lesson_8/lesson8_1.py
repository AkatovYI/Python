#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, mon, year):
        self.day = day
        self.mon = mon
        self.year = year

    @classmethod
    def number(cls, data):
        day, mon, year = data.split('-')
        return Data.err(int(day), int(mon), int(year))

    @staticmethod
    def err(day, mon, year):
        if 1 < day and day > 31:
            return f'Не правильная дата'
        if 1 < mon and mon > 12:
            return f'Не правильный месяц'
        if 1 < year and year > 9999:
            return f'Не правильный год'
        return f'{day} - {mon} - {year}'


print(Data.number('26-11-2020'))
print(Data.number('32-11-2020'))
print(Data.number('26-14-2020'))
print(Data.number('26-11-12020'))




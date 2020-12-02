# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
import copy

class Warehous():
    ''' Класс складского учета'''

    def __init__(self, data):
        self.data = data

    def add(self, kod, add_data):
        self.data.append([kod, add_data])

    def war(self):
        my_data = (('принтер', {'наименование': [], 'цена': [], 'количество': []}),
                   ('сканер', {'наименование': [], 'цена': [], 'количество': []}),
                   ('ксерокс', {'наименование': [], 'цена': [], 'количество': []}),)
        for el in self.data:
            if el[0] == 'склад':
                if el[1]['тип'] == 'принтер':
                    my_data[0][1]['наименование'].append(el[1]['name'])
                    my_data[0][1]['цена'].append(el[1]['цена'])
                    my_data[0][1]['количество'].append(el[1]['количество'])
                elif el[1]['тип'] == 'сканер':
                    my_data[1][1]['наименование'].append(el[1]['name'])
                    my_data[1][1]['цена'].append(el[1]['цена'])
                    my_data[1][1]['количество'].append(el[1]['количество'])
                elif el[1]['тип'] == 'ксерокс':
                    my_data[2][1]['наименование'].append(el[1]['name'])
                    my_data[2][1]['цена'].append(el[1]['цена'])
                    my_data[3][1]['количество'].append(el[1]['количество'])
        for el in my_data:
            print(f'{el[0]}: {el[1]}')

    def transfer(self, podr, type, name, price, kol):
        for i, el in enumerate(self.data):
            if el[1]['тип'] == type and el[1]['name'] == name and el[1]['цена'] == price and el[1]['количество'] >= kol:
                if el[1]['количество'] == kol:
                    self.data[i][0] = podr
                    break
                else:
                    my_str = copy.deepcopy(el)
                    self.data[i][0] = podr
                    self.data[i][1]['количество'] = kol
                    my_str[1]['количество'] -= kol
                    self.data.append(my_str)

    def prn(self):
        for el in self.data:
            print(f'{el[0]}: {el[1]}')


class OfficeEq():
    ''' Класс оргтехника'''
    stukt = {'name': '',
             'size_p': 'A4',
             'year': 2000}


class Prints(OfficeEq):
    ''' Класс принтера'''
    stukt = OfficeEq.stukt.copy()

    def __init__(self, name, size_p='A4', year=2020, type_prints='Лазерный'):
        super().__init__()
        self.stukt['name'] = name
        self.stukt['size_p'] = size_p
        self.stukt['year'] = year
        self.stukt.update({'type_prints': type_prints})


class Scans(OfficeEq):
    ''' Класс сканеры'''
    stukt = OfficeEq.stukt.copy()

    def __init__(self, name, size_p='A4', year=2020, type_scans='Настольный'):
        super().__init__()
        self.stukt['name'] = name
        self.stukt['size_p'] = size_p
        self.stukt['year'] = year
        self.stukt.update({'type_scans': type_scans})


class Xeroxs(OfficeEq):
    ''' Класс ксероксы'''
    stukt = OfficeEq.stukt.copy()

    def __init__(self, name, size_p='A4', year=2020, type_xeroxs='Настольный'):
        super().__init__()
        self.stukt['name'] = name
        self.stukt['size_p'] = size_p
        self.stukt['year'] = year
        self.stukt.update({'type_xeroxs': type_xeroxs})


print('Программа складского учета')
print(f'Для выбора действия нажмите: 1 - прием товара на склад,\n'
      f'                             2 - передача товара со склада в подразделение,\n'
      f'                             3 - печать состояния склада,\n'
      f'                             4 - печать всей оргтехники,\n'      
      f'                             0 - выход из программы')

my_stru = []
my_war = Warehous(my_stru)
while True:
    m = input('Для выхода из программы нажмите "0", для продолжения 1, 2, 3 или 4: ')
    if m == '0':
        break
    elif m == '1':
        my_warehous = {'тип': '', 'цена': 0.0, 'количество': 0}
        for key in my_warehous:
            if key == 'тип':
                el = input(key + ' (принтер, сканер, ксерокс): ')
            else:
                el = input(key + ': ')
            if key == 'цена':
                try:
                    el = float(el)
                except ValueError as err:
                    print(f'Вы ввели не правильный символ, должно быть число - {err}')
                    continue
            elif key == 'количество':
                try:
                    el = int(el)
                except ValueError as err:
                    print(f'Вы ввели не правильный символ, должно быть число - {err}')
                    continue
            my_warehous[key] = el
        if my_warehous['тип'] == 'принтер':
            print('Введите через пробел наименование принтера, размер бумаги, год выпуска, тип принтера:')
            print('Например: HP A4 2019 лазерный')
            name, size_p, year, type_prints = input('').split()
            Prints(name, size_p, year, type_prints)
            my_warehous.update(Prints.stukt)
        elif my_warehous['тип'] == 'сканер':
            print('Введите через пробел наименование сканера, размер бумаги, год выпуска, тип сканера:')
            print('Например: HP A4 2019 настольный')
            name, size_p, year, type_scans = input('').split()
            Scans(name, size_p, year, type_scans)
            my_warehous.update(Scans.stukt)
        elif my_warehous['тип'] == 'ксерокс':
            print('Введите через пробел наименование ксерокса, размер бумаги, год выпуска, тип ксерокса:')
            print('Например: Epson A4 2020 настольный')
            name, size_p, year, type_xeroxs = input('').split()
            Xeroxs(name, size_p, year, type_xeroxs)
            my_warehous.update(Xeroxs.stukt)
        else:
            print('Вы ввели не правильный тип оборудования')
            continue
        my_war.add('склад', my_warehous)
    elif m == '2':
        print('На текущий момент на складе находится:')
        my_war.war()
        print(
            'Выберите оргтехнику для передачи в подразделение в формате: подразделение, тип, наименование, цена, количество:')
        print('Например: IT принтер Epson 2000 2')
        podr, type, name, price, kol = input().split()
        try:
            price = float(price)
            kol = int(kol)
        except ValueError as  err:
            print(f'Вы ввели не правильный символ, должно быть число - {err}')
            continue
        my_war.transfer(podr, type, name, price, kol)
        print('На складе осталось:')
        my_war.war()
    elif m == '3':
        print('Состояние склада:')
        my_war.war()
    elif m == '4':
        print('Отладочная информация:')
        my_war.prn()
    else:
        print('Введена не правильная команда')

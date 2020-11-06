# 6)	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#    “название”: [“компьютер”, “принтер”, “сканер”],
#    “цена”: [20000, 6000, 2000],
#    “количество”: [5, 2, 7],
#    “ед”: [“шт.”]
# }


print('Программа обработки данных "Товары"')
print('Сформируйте структуду данных по единице товара')
print('Окончание ввода пустая строка в названии')
my_list = []
i = 1
while True:
    my_stru = {'название': '', 'цена': 0, 'количество': 0, 'ед': ''}
    for key in my_stru:
        el = input(key + ': ')
        if key == 'название' and el == '':
            break
        if type(my_stru.setdefault(key)) == int:
            el = int(el)
        my_stru[key] = el
    if key == 'название' and el == '':
        break
    my_list.append((i, my_stru))
    i += 1

my_stru = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for el in my_list:
    my_stru['название'].append(el[1]['название'])
    my_stru['цена'].append(el[1]['цена'])
    my_stru['количество'].append(el[1]['количество'])
    my_stru['ед'].append(el[1]['ед'])

print()
for el in my_stru.items():
    print(el)

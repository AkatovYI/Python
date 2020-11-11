# 2)	Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Для ввода списка')
list_old = []
while True:
    elem = input('Введите любое число, окончание ввода пустой символ: ')
    if elem == '':
        break
    else:
        list_old.append(elem)

i = 1
list_new = []
new = list_old[0]
for elem in list_old:
    if i % 2 == 0:
        list_new.append(elem)
        list_new.append(new)
        i += 1
    else:
        new = elem
        i += 1
if i % 2 == 0:
    list_new.append(new)

print('Исходный список: ', list_old)
print('Полученный список: ', list_new)

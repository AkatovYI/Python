# 3)	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

mes = int(input('Введите номер месяца от 1 до 12: '))
while True:
    if mes < 1 or mes > 12:
        mes = int(input('Введите номер месяца от 1 до 12: '))
    else:
        break

list_mes = ['зима', 'весна', 'лето', 'осень']
dict_mes = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень'
}
vrem = 1
vrem = 1 if mes == 12 or mes == 1 or mes == 2 else vrem
vrem = 2 if mes == 3 or mes == 4 or mes == 5 else vrem
vrem = 3 if mes == 6 or mes == 7 or mes == 8 else vrem
vrem = 4 if mes == 9 or mes == 10 or mes == 11 else vrem
print(f'Список - {list_mes[vrem - 1]}, Словарь - {dict_mes.get(vrem)}')

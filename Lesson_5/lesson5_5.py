#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from  random import randint

t_new = open('text_5.txt', 'w', encoding='utf-8')
t_new.writelines(str(randint(0, 100)) + ' ' for _ in range(20))
t_new.close()

with open('text_5.txt', 'r', encoding='utf-8') as t_new:
    summ = 0
    for el in t_new:
        el_n = el.split()
        print(f'Полученная последовательность: {el}')
        for x in el_n:
            summ += int(x)

print(f'Сумма всех чисел: {summ}')
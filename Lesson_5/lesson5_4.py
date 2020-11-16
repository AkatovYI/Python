#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

from translate import Translator as ts
ts =ts(from_lang='en', to_lang='ru')

t_new = open('text_41.txt', 'w', encoding='utf-8')
with open('text_4.txt', 'r', encoding='utf-8') as t:
    for el in t:
        el_1, el_2, el_3 = el.split()
        tr = ts.translate(el_1)
        t_new.write(f'{tr} {el_2} {el_3}\n')

t_new.close()

t_new = open('text_42.txt', 'w', encoding='utf-8')
with open('text_4.txt', 'r', encoding='utf-8') as t:
    for el in t:
        el_1, el_2, el_3 = el.split()
        if int(el_3) == 1:
            el_1 = 'Один'
        elif int(el_3) == 2:
            el_1 = 'Два'
        elif int(el_3) == 3:
            el_1 = 'Три'
        else:
            el_1 = 'Четыре'
        t_new.write(f'{el_1} {el_2} {el_3}\n')

t_new.close()
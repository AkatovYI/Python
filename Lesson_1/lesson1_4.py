# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Введите число: '))
num_o = num
if num_o < 10:
    num_s = num_o
else:
    num_s = num_o % 10
    num_o = num_o // 10

while True:
    if num_o < 10:
        if num_s < num_o:
            num_s = num_o
        break
    else:
        num_ss = num_o % 10
        num_o = num_o // 10
    if num_s < num_ss:
        num_s = num_ss

print(f'Наибольшее число {num_s}')


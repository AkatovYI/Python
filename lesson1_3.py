#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = input('Введите число: ')
result = int(num) + int(num + num) + int(num + num + num)
print(f'Результат: {num} + {num + num} + {num + num + num} = {result}')
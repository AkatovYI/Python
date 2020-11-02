#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.


sec_new = int(input('Введите время в секундах: '))
hour = (sec_new // 3600)
minutes = ((sec_new - hour * 3600) // 60)
sec = ((sec_new - hour * 3600) % 60)
if hour < 10:
    hour_s = '0' + str(hour)
else:
    hour_s = str(hour)
if minutes < 10:
    minutes_s = '0' + str(minutes)
else:
    minutes_s = str(minutes)
if sec < 10:
    sec_s = '0' + str(sec)
else:
    sec_s = str(sec)

print(f'Полученное время {hour_s}:{minutes_s}:{sec_s}')
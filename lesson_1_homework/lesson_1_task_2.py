# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Запрос на ввод времени в секундах:

while True:
    time_sec = input('Введите промежуток времени в секундах (целое число секунд):\n')

    # Делаем проверку на ввод числа
    if time_sec.isdigit():
        break
    else:
        print('Не было введено целое положительное число')

# Преобразуем введенную строку в число
time_sec = int(time_sec)

# Определим количество часов
time_hours = time_sec // 3600

# Определим, сколько секунд нам остается проанализировать для деления на минуты и секунды
time_sec_part2 = time_sec - time_hours * 3600

# Определим количество минут в оставшейся части
time_min = time_sec_part2 // 60

# Определим остаток секунд для его вывода
time_sec_part3 = time_sec_part2 - time_min * 60

# Форматный вывод результатов
print(f'Время: {time_hours:02}:{time_min:02}:{time_sec_part3:02}')
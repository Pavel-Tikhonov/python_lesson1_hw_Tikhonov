# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# Объявление переменных:
var1 = 1
var2 = 2.5
var3 = True
var4 = None
var5 = 'Строка'

# Вывод переменных на экран:
print(var1, var2, var3, var4, var5, sep=',')

# Запрос у пользователя чисел и строк, сохранение всего этого в переменные:
var1 = input('Введите первое число:\n')
var2 = input('Введите второе число:\n')

if var1.isdigit():
    var1 = int(var1)
else:
    var1 = 'Не было введено первое число'

if var2.isdigit():
    var2 = int(var2)
else:
    var2 = 'Не было введено второе число'

var3 = input('Введите первую строку:\n')
var4 = input('Введите вторую строку:\n')

# Вывод всего этого на экран:
print(var1, var2, var3, var4, sep=',')
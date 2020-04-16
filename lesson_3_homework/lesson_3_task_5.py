# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
breaker_flag = 0
result = 0
while True:
    numbers_str = input('Введите строку чисел, разделенную пробелами:\n')
    if numbers_str.find('@') == 0:
        print('Обнаружен символ "@". Программа завершает работу.')
        break

    numbers_str_list = numbers_str.split(' ')

    try:
        numbers_str_list.index('@')
    except ValueError:
        limit = len(numbers_str_list)
    else:
        limit = numbers_str_list.index('@')
        breaker_flag += 1

    numbers_float_list = map(lambda x: float(x), numbers_str_list[:limit])
    result = result + sum(numbers_float_list)
    if breaker_flag > 0:
        print('Обнаружен символ "@". Программа завершает работу.')
        break
    print(result)
    print('Продолжите ввод строки чисел или введите "@" для выхода')
print(f'Вы вышли из программы. Крайний результат составил {result}')

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    divide_1 = input('Введите делимое:\n')
    divide_2 = input('Введите делитель:\n')
    try:
        divide_1, divide_2 = float(divide_1), float(divide_2)
        if not divide_2:
            raise MyException('Ошибка. На ноль делить нельзя!')
    except ValueError as e:
        print(f'Ошибка: {e}. В качестве делимого и делителя должно выступать число.')
    except MyException as e:
        print(e)
    else:
        break

print(f'{divide_1} / {divide_2} = {divide_1 / divide_2}')




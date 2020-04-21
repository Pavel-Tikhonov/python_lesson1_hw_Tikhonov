# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial


def fibo_gen(factorial_number):
    """Функция возвращает генератор, состоящий из первых 15 чисел - элементов факториала числа, выступающего в роли
    входного параметра.
    Позиционный параметр:
    :param factorial_number: int - факториал числа
    :yield : generator object
    """

    try:
        factorial_number = int(factorial_number)
    except ValueError as e:
        print(f'Возникла ошибка с входным аргументом: {e}\nВходной аргумент должен представлять собой целое число.\n')
        return None
    tmp = factorial_number
    for itm in count(1):
        tmp /= itm
        if tmp == 1:
            break

    print(f'На вход функции было подано число {factorial_number}. Это есть факториал числа {itm}.\n'
          f'Однако если это число больше 15, мы вам покажем только первые 15 чисел!')
    if itm > 15:
        n = 15
    else:
        n = itm

    for itm in range(1, n + 1):
        yield itm


x = factorial(20)

for el in fibo_gen(x):
    print(el)

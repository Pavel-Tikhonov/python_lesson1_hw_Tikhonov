# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count
from sys import argv
from time import sleep

# argv = ['_', 5]

try:
    argv[1] = int(argv[1])
    for itm in count(argv[1]):
        print(itm)
        sleep(1)
except ValueError as e:
        print(f'Возникла ошибка с входным аргументом: {e}\nВходной аргумент должен представлять собой целое число.\n')
except KeyboardInterrupt:
        print(f'Уже уходите? Ну ладно.\n')


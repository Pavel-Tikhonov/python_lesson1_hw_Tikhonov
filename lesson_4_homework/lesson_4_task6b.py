# 6. Реализовать два небольших скрипта:
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle
from time import sleep

my_list = [1, 2, 3, 4, 5]

for itm in cycle(my_list):
    print(itm)
    sleep(1)

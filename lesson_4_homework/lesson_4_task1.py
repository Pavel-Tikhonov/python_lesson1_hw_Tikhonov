# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def profit_count(production, rate, premium):
    """Функция возвращает величину заработной платы сотрудника.
    Функция расчитана на ее вызов из терминала с указанием входных параметров.
    Позиционные параметры:
    :param production: float - выработка в часах
    :param rate: float - ставка в часах
    :return premium: float - премия
    """
    profit = production * rate + premium
    return profit


production = argv[1]
rate = argv[2]
premium = argv[3]

profit = profit_count(production, rate, premium)
print(f'Были введены следующие данные:\n'
      f'Выработка: {production} ч.\n'
      f'Ставка: {rate} ч.\n'
      f'Премия: {premium} гривен\n'
      f'Имеем заработок в размере {production}*{rate} + {premium} = {profit} гривен')

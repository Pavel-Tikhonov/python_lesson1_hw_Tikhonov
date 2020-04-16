# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func_divide(var1: float, var2: float):
    """Функция возвращает частное от деления var1 на var2.

    Позиционные параметры:
    :param var1: float
    :param var2: float
    :return divide_result: float

    """

    try:
        var1 = float(var1)
    except ValueError as e:
        print(f'Возникла ошибка с первым аргументом: {e}\nВходные данные должны относиться к классу float.')
        return None
    try:
        var2 = float(var2)
    except ValueError as e:
        print(f'Возникла ошибка со вторым аргументом: {e}\nВходные данные должны относиться к классу float.')
        return None
    try:
        divide_result = var1 / var2
    except ZeroDivisionError as e:
        print(f'Возникла ошибка при расчете результата: {e}\nНа ноль делить нельзя.')
    else:
        return divide_result


while True:
    arg1 = input('Введите делимое:\n')
    arg2 = input('Введите делитель:\n')
    result = my_func_divide(arg1, arg2)
    if result != None:
        print(f'Деление прошло успешно.\n{arg1} / {arg2} = {result:<.3f}')
        break





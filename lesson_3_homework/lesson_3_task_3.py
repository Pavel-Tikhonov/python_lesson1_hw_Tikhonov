# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(var1: float, var2: float, var3: float):
    """Функция принимает три позиционных аргумента и возвращает сумму двух наибольших из них.

    Позиционные параметры:
    :param var1: float
    :param var2: float
    :param var3: float
    :return sum_result: float

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
        var3 = float(var3)
    except ValueError as e:
        print(f'Возникла ошибка с третим аргументом: {e}\nВходные данные должны относиться к классу float.')
        return None

    var_list = [var1, var2, var3]
    min_var = min(var_list)
    var_list.remove(min_var)
    sum_result = sum(var_list)

    return sum_result


arg1 = "1"
arg2 = 2
arg3 = 3
result = my_func(arg1, arg2, arg3)
if result != None:
    print(f'Функции my_func были переданы следующие значения: {arg1}, {arg2}, {arg3}.\n'
          f'Результат работы функции: сумма двух набольших аргументов равна {result}')
else:
    print('Из-за наличия одной или нескольких ошибок при вводе входных данных работа функции была прекращена.')

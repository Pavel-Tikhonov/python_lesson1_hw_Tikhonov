# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.


class Cell:
    def __init__(self, alveolas):
        self.alveolas = alveolas

    def __add__(self, other):
        return Cell(self.alveolas + other.alveolas)

    def __sub__(self, other):
        delta = self.alveolas - other.alveolas
        if delta < 0:
            print('Вычитание клеток провести не удалось: Количество ячеек клетки слева меньше, чем у клетки справа.')
            return None
        else:
            return Cell(delta)

    def __mul__(self, other):
        return Cell(self.alveolas * other.alveolas)

    def __truediv__(self, other):
        delta = self.alveolas / other.alveolas
        return Cell(round(delta))

    def make_order(self, alveolas_raw):
        if alveolas_raw <= 0:
            return None
        total_alveolas = self.alveolas
        raw_number = round(total_alveolas / alveolas_raw)
        alveolas_matrix = []
        for i in range(raw_number):
            if 0 < total_alveolas < alveolas_raw:
                alveolas_raw = total_alveolas
            raw_list = ['*' for _ in range(alveolas_raw)]
            raw_list_str = " ".join(raw_list)
            alveolas_matrix.append(raw_list_str)
            total_alveolas -= alveolas_raw
        return '\n'.join(alveolas_matrix)


c1 = Cell(5)
c2 = Cell(3)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 / c2
print(f'Число ячеек клетки №1 равно {c1.alveolas}.')
print(f'Число ячеек клетки №2 равно {c2.alveolas}.')
print(f'Результат сложения клеток №1 и №2 - есть клетка №3 с числом ячеек {c3.alveolas}.')
try:
    print(f'Результат вычитания клетки №2 из клетки №1 - есть клетка №4 с числом ячеек {c4.alveolas}.')
except AttributeError:
    print('При вычитании клеток возникла ошибка: количество ячеек клетки слева меньше, чем у клетки справа.')
print(f'Результат умножения клеток №1 и №2 - есть клетка №5 с числом ячеек {c5.alveolas}.')
print(f'Результат деления клеток №1 и №2 - есть клетка №3 с числом ячеек {c6.alveolas}.')

c7 = Cell(13)
n_raw = 5
print(f'Проверим метод make_order. Создана клетка №7 с числом ячеек {c7.alveolas}.\n'
      f'Имеем результат метода для числа ячеек в ряду, равном {n_raw}:\n')
if c7.make_order(n_raw):
    print(c7.make_order(n_raw))
else:
    print('Возникла ошибка метода: число ячеек в ряду должно быть больше 0')





# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        m_list_str = []
        for list_el in self.m_list:
            list_el = map(str, list_el)
            m_raw = " ".join(list_el)
            m_list_str.append(m_raw)
        return '\n'.join(m_list_str)

    def __add__(self, other):
        sum_matrix = []
        for i, raw_1 in enumerate(self.m_list):
            sum_raw = []
            for j, raw_1_itm in enumerate(raw_1):
                sum_el = raw_1_itm + other.m_list[i][j]
                sum_raw.append(sum_el)
            sum_matrix.append(sum_raw)
        return Matrix(sum_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(f'Матрица 1:\n{m1}\n')
m2 = Matrix([[7, 8, 9], [10, 11, 12]])
print(f'Матрица 2:\n{m2}\n')
m3 = m1 + m2
print(f'Сумма m1 + m2:\n {m3}')

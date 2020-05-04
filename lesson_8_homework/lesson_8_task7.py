# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# Для работы с комплексными числами имеем следующие арифметические операции в общем виде:
# Пусть имеются два комплесных числа: a + bj; c + dj; Причем: j^2 = -1
# Тогда:
# Сложение: (a + bj) + (c + dj) = (a + c) + (b + d)j
# Вычитание: (a + bj) - (c + dj) = (a - c) + (b - d)j
# Умножение: (a + bj) * (c + dj) = ac + adj + bcj + bdj^2 = (ac - bd) + (bc + ad)j
# Деление: (a + bj) / (c + dj) = (a + bj) / (c + dj) * (c - dj) / (c - dj) =
# = (ac + bd) / (c^2 + d^2) + ((bc - ad) / (c^2 + d^2))j


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        result_real = self.real + other.real
        result_imag = self.imag + other.imag
        return result_real, result_imag

    def __sub__(self, other):
        result_real = self.real - other.real
        result_imag = self.imag - other.imag
        return result_real, result_imag

    def __mul__(self, other):
        # a + bj; c + dj;
        # (ac - bd) + (bc + ad)j
        result_real = self.real * other.real - self.imag * other.imag
        result_imag = self.imag * other.real + self.real * other.imag
        return result_real, result_imag

    def __truediv__(self, other):
        # a + bj; c + dj;
        # = (ac + bd) / (c^2 + d^2) + ((bc - ad) / (c^2 + d^2))j
        result_real = (self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2)
        result_imag = (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2)
        return result_real, result_imag

    def __str__(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}j'
        else:
            return f'{self.real} - {self.imag * -1}j'


n1 = ComplexNumber(2, 3)
n2 = ComplexNumber(1, -4)
print(f'Число 1: {n1}\nЧисло 2: {n2}')
result_add = n1 + n2
print(f'Сложение: {result_add} --> {result_add[0]} + {result_add[1]}j')
result_sub = n1 - n2
print(f'Вычитание: {result_sub} --> {result_sub[0]} + {result_sub[1]}j')
result_mul = n1 * n2
print(f'Умножение: {result_mul} --> {result_mul[0]:<.1f} + {result_mul[1]:<.1f}j')
result_tdiv = n1 / n2
print(f'Деление: {result_tdiv} --> {result_tdiv[0]:<.1f} + {result_tdiv[1]:<.1f}j')


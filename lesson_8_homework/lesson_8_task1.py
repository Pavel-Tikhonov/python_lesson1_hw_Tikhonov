# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_info(cls, date_str):
        info_dict = {}
        info_str_list = date_str.split('-')
        info_int_list = list(map(int, info_str_list))
        info_dict['day'] = info_int_list[0]
        info_dict['month'] = info_int_list[1]
        info_dict['year'] = info_int_list[2]
        return info_dict

    @staticmethod
    def date_validation(date_str):
        info_str_list = date_str.split('-')
        day_valid = str(int(info_str_list[0]))
        month_valid = str(int(info_str_list[1]))
        year_valid = str(int(info_str_list[2]))
        date_valid = '-'.join([day_valid, month_valid, year_valid])
        return date_valid


info_str = '02-05-2020'
d = Date(info_str)
print(f'Имеется дата: {d.date_str}')
print(f'Результат метода date_info:\n{Date.date_info(d.date_str)}')
print(f'Результат метода date_validation:\n{Date.date_validation(d.date_str)}')




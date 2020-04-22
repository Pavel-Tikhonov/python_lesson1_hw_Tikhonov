# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

file_name1 = 'file_for_task7_read.txt'
file_name2 = 'file_for_task7_write.json'

name_profit_dict = {}
a_profit_dict = {}
profits_list_tmp = []
with open(file_name1, 'r') as my_file_read:
    print(f'В исходном файле имеется следующая информация:\n\n{my_file_read.read()}')
    my_file_read.seek(0)
    for line in my_file_read:
        line_info = line.replace('.', '').replace('\n', '').split(' ')
        firm_name = line_info[0]
        firm_gain = float(line_info[2])
        firm_los = float(line_info[-1])
        firm_profit = firm_gain - firm_los
        profits_list_tmp.append(firm_profit)
        name_profit_dict[firm_name] = firm_profit

profits_list = [itm for itm in profits_list_tmp if itm > 0]
average_profit_number = sum(profits_list) / len(profits_list)
a_profit_dict['average_profit'] = average_profit_number

result_list = [name_profit_dict, a_profit_dict]
print(f'\nВ результате преобразований был составлен список:\n{result_list}\n')

with open(file_name2, 'w+') as my_file_write:
    json.dump(result_list, my_file_write)
    my_file_write.seek(0)
    print(f'После создания json-файла в него была записана строка соответсвующего формата:\n{json.load(my_file_write)}')





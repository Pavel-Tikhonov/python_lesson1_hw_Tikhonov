# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

rand_list = [randint(1, 10) for itm in range(10)]
print(f'Имеется набор чисел: {rand_list}')

file_name = 'file_for_task5.txt'
with open(file_name, 'w+', encoding='UTF-8') as my_file:
    rand_str = ' '.join(map(str, rand_list))
    my_file.write(f'{rand_str}')
    print(f'В новый файл была записана следующая строка:\n{rand_str}')
    my_file.seek(0)
    read_str = my_file.readline()
    print(f'Из файла была считана следующая строка:\n{read_str}')
    read_list = list(map(int, read_str.split(' ')))
    print(f'Эта строка была преобразована в список чисел:\n{read_list}')
    file_list_sum = sum(read_list)
    print(f'Таким образом, сумма чисел в файле равна {file_list_sum}')


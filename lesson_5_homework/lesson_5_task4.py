# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

file_name1 = 'file_for_task4_read.txt'
file_name2 = 'file_for_task4_write.txt'
rus_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
with open(file_name1, 'r', encoding='UTF-8') as my_file_read:
    print(f'В исходном файле содержится следующая информация:\n{my_file_read.read()}')
    my_file_read.seek(0)
    with open(file_name2, 'w+', encoding='UTF-8') as my_file_write:
        for line in my_file_read:
            key_name = line.split(' - ')[-1].replace('\n', '')
            itm_name = line.split(' - ')[0]
            my_file_write.write(line.replace(itm_name, rus_dict[key_name]))

        my_file_write.seek(0)
        print(f'В новом файле содержится следующая информация:\n{my_file_write.read()}')



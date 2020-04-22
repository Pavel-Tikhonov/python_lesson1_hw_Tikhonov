# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file_name = 'file_for_task2.txt'

with open(file_name, 'r') as my_file:
    print(f'В файле содержится следующая информация:\n{my_file.read()}')
    my_file.seek(0)
    file_info = {}
    for i, line in enumerate(my_file, 1):
        file_info[f'Строка {i}'] = f'Длина строки составляет {len(line)} симола(ов)'
    for key, itm in file_info.items():
        print(f'{key} -- {itm}')


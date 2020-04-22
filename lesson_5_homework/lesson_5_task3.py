# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

file_name = 'file_for_task3.txt'
with open(file_name, 'r') as my_file:
    print(f'В файле содержится следующая информация:\n{my_file.read()}')
    my_file.seek(0)
    profit_list = []
    names_list = []
    for line in my_file:
        words_list = line.replace('\n', '').split(': ')
        if len(words_list) > 1:
            profit_tmp = float(words_list[1])
            profit_list.append(profit_tmp)
            if profit_tmp < 20000:
                names_list.append(words_list[0])

    average_profit = sum(profit_list) / len(profit_list)
    print(f'Фамилии сотрудников, оклад которых менее 20000:\n{names_list}\n'
          f'При этом средний оклад среди всех сотрудников составляет: {average_profit}')


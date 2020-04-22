# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


file_name = 'file_for_task1.txt'

try:
    file = open(file_name, 'w+')
    while True:
        some_str = input('Введите то, что хотите записать в файл.\nЕсли запишите пустую строку, работа закончится.\n')
        if some_str:
            file.write(f'{some_str}\n')
        else:
            print('Вы ввели пустую строку. Программа заканчивает работу.')
            break
except IOError as e:
    print(f'Обнаружена ошибка ввода-вывода: {e}')
except NameError as e:
    print(f'Не могу создать новый файл: {e}')
finally:
    file.seek(0)
    print(f'В файле содержится следующая информация:\n{file.read()}')
    file.close()








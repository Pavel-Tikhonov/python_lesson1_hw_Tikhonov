# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Формирование списка через input
check_list = []

while True:
    list_length = input('Введите количество элементов в будущем списке:\n')
    if list_length.isdigit():
        list_length = int(list_length)
        break
    else:
        print('Не было введено целое положительное число.')

for i in range(list_length):
    check_list.append(input(f'Введите {i + 1}-й элемент списка:\n'))

print(f'Был введен список: {check_list}')

# Меняем местами соседние элементы списка
for i in range(1, len(check_list), 2):
    list_element = check_list.pop(i)
    check_list.insert(i - 1, list_element)

print(f'После преобразований имеем: {check_list}')


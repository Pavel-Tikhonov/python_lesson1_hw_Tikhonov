
participates_list = []
participates = int(input('Введите количество участников:\n'))
i = participates

while i >= 1:
    participate = input('Кто занял {} место?\n'.format(i))
    participates_list.append(participate)
    i -= 1
print('В конкурсе учавствовали: {}'.format(participates_list))
participates_list.reverse()
print('Призеры с 1 по 3 место: {}'.format(participates_list[:3]))
print(f'Победители {participates_list[0]}, {participates_list[1]}, {participates_list[2]}. Поздравляем!')





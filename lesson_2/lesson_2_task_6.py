# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


products_list = []
product_dict = {}
while True:
    product_number = input('Сколько позиций товара вы хотите добавить?:\n')
    if product_number.isdigit():
        product_number = int(product_number)
        break
    else:
        print('Не было введено целое положительное число.')

for i in range(1, product_number + 1):
    product_name = input(f'Введите название {i}-го товара:\n')

    while True:
        product_price = input(f'Введите цену {i}-го товара:\n')
        if product_price.isdigit():
            product_price = int(product_price)
            break
        else:
            print('Не было введено целое положительное число.')

    while True:
        product_quantity = input(f'Введите количество единиц {i}-го товара:\n')
        if product_quantity.isdigit():
            product_quantity = int(product_quantity)
            break
        else:
            print('Не было введено целое положительное число.')

    product_measurement = input(f'Введите единицу измерения количества {i}-го товара:\n')
    product_tuple = (i, {'название': product_name,
                         'цена': product_price,
                         'количество': product_quantity,
                         'ед': product_measurement})
    products_list.append(product_tuple)


print(f'В результате имеем следующий список товаров с их характеристиками:')
for i in range(product_number):
    print(products_list[i])

product_dict_result = {}
product_name_all = []
product_price_all = []
product_quantity_all = []
product_measurement_all = []

print('Имеем итоговый словарь с характеристиками товаров:')
for i in range(product_number):
    product_name_all.append(products_list[i][1]['название'])
    product_price_all.append(products_list[i][1]['цена'])
    product_quantity_all.append(products_list[i][1]['количество'])
    product_measurement_all.append(products_list[i][1]['ед'])

product_dict_result['название'] = list(set(product_name_all))
product_dict_result['цена'] = product_price_all
product_dict_result['количество'] = product_quantity_all
product_dict_result['ед'] = list(set(product_measurement_all))

for key, value in product_dict_result.items():
    print(f'{key}: {value}')



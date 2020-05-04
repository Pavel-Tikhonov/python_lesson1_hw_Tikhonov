# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Storage:
    def __init__(self, name, address, tel):
        self.name = name
        self.address = address
        self.tel = tel
        self.storage_list = []

    def add_equip(self, *args):
        storage_list_new = []
        for itm in args:
            storage_list_new.append(itm)
        self.storage_list.extend(storage_list_new)
        print(f'В хранилище {self.name} были добавлены следующие позиции:\n',
                     '\n'.join(list(map(str, storage_list_new)))
              )
        return None

    @property
    def get_storage_info(self):
        if len(self.storage_list):
            print(f'В хранилище {self.name} имеются следующие позиции:\n',
                  '\n'.join(list(map(str, self.storage_list)))
                  )
            return self.storage_list
        else:
            print(f'На данный момент в хранилище {self.name} нет ни одной позиции.')
            return None

    def equip_exchange(self, other, *args):
        list_of_changes = []
        other.add_equip(*args)
        for itm in args:
            list_of_changes.append(itm)
            self.storage_list.remove(itm)
        print(f'Из хранилища {self.name} были удалены следующие позиции:\n',
              '\n'.join(list(map(str, list_of_changes)))
              )
        return None


class Equipment:
    def __init__(self, name, id, quantity, **kwargs):
        self.name = name
        self.id = id
        self.quantity = quantity
        for key, itm in kwargs.items():
            setattr(self, key, itm)

    def __str__(self):
        atr_dict = {}
        atr_list = [arg for arg in dir(self) if not arg.startswith('_')]
        for itm in atr_list:
            atr_dict[itm] = getattr(self, itm)
        return str(atr_dict)


class Printer(Equipment):
    def __init__(self, name, id, quantity, **kwargs):
        super().__init__(name, id, quantity, **kwargs)


class Scanner(Equipment):
    def __init__(self, name, id, quantity, **kwargs):
        super().__init__(name, id, quantity, **kwargs)


st1 = Storage('Склад №1', 'ул.Ленина д.54', '12345')

while True:
    while True:
        obj_type = input('Какой тип товара вы хотите добавить? (1 - принтер, 2 - сканнер):\n')
        if not(len(obj_type) == 1 and '1' in obj_type or '2' in obj_type):
            print('Введите либо "1" либо "2".')
            continue
        obj_quantity = input('Введите количество товара:\n')
        try:
            int(obj_quantity)
        except ValueError as e:
            print(f'Ошибка: {e}. В качестве количества товара должно выступать число.')
            continue
        else:
            obj_name = input('Введите название товара:\n')
            obj_id = input('Введите id товара:\n')
            break
    answer = input('Хотите ввести дополнительные характеристики товара? (пустая строка означает "нет")\n')
    if answer:
        char_dict = {}
        while True:
            char_name = input('Введите название характеристики:\n')
            char_value = input('Введите значение характеристики:\n')
            char_dict[char_name] = char_value
            answer = input('Хотите ввести дополнительные характеристики товара? (пустая строка означает "нет")\n')
            if not answer:
                break

    if obj_type == '1':
        try:
            char_dict
        except NameError:
            obj = Printer(obj_name, obj_id, obj_quantity)
        else:
            obj = Printer(obj_name, obj_id, obj_quantity, **char_dict)
    else:
        try:
            char_dict
        except NameError:
            obj = Scanner(obj_name, obj_id, obj_quantity)
        else:
            obj = Scanner(obj_name, obj_id, obj_quantity, **char_dict)

    print(f'Был создан объект:\n{obj}')
    st1.add_equip(obj)
    info1 = st1.get_storage_info
    answer = input('Хотите добавить еще позицию? (пустая строка значит "нет")')
    if not answer:
        break

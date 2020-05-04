# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


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
    def __init__(self, name, id, quantity):
        self.name = name
        self.id = id
        self.quantity = quantity


class Printer(Equipment):
    def __init__(self, printing_type,  name, id, quantity):
        self.printing_type = printing_type
        super().__init__(name, id, quantity)

    def __str__(self):
        eq_dict = {'name': self.name,
                    'id': self.id,
                    'quantity': self.quantity,
                    'printing_type': self.printing_type
                   }
        return str(eq_dict)


class Scanner(Equipment):
    def __init__(self, light_source,  name, id, quantity):
        self.light_source = light_source
        super().__init__(name, id, quantity)

    def __str__(self):
        eq_dict = {'name': self.name,
                    'id': self.id,
                    'quantity': self.quantity,
                    'light_source': self.light_source
                   }
        return str(eq_dict)


pr1 = Printer('laser', 'Printer Samsung GT100', '001', 50)
pr2 = Printer('inject', 'Printer Cannon RGD300', '002', 25)
pr3 = Printer('laser', 'Printer Sony MT200', '003', 10)

sc1 = Scanner('LED', 'Scanner Sony F100', '004', 5)
sc2 = Scanner('FLU', 'Scanner Cannon D554', '005', 9)
sc3 = Scanner('XE', 'Scanner Sony C125', '006', 13)

st1 = Storage('Склад №1', 'ул.Ленина д.54', '12345')
st1.add_equip(pr1, pr2, pr3)
info1 = st1.get_storage_info
st1.add_equip(sc1, sc2, sc3)
info2 = st1.get_storage_info

st2 = Storage('Подразделение №1', 'ул.Сталина д.45', '54321')
info3 = st2.get_storage_info
st1.equip_exchange(st2, pr1, pr2, pr3)
info4 = st2.get_storage_info
info5 = st1.get_storage_info

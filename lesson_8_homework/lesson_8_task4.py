# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Storage:
    def __init__(self, *args):
        self.args = args


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


pr1 = Printer('laser', 'Samsung GT100', '001', 50)
pr2 = Printer('inject', 'Cannon RGD300', '002', 25)
pr3 = Printer('laser', 'Sony MT200', '003', 10)

sc1 = Scanner('LED', 'Sony F100', '004', 5)
sc2 = Scanner('FLU', 'Cannon D554', '005', 9)
sc3 = Scanner('XE', 'Sony C125', '006', 13)


storage_main = Storage(pr1, pr2, pr3, sc1, sc2, sc3)

print('После формирования объектов склад содержит следующие товары:')
for i in range(6):
    print(storage_main.args[i])

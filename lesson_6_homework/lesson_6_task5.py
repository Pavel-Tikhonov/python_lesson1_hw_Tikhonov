# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запускаю отрисовку для класса Stationery.')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запускаю отрисовку для класса Pen')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запускаю отрисовку для класса Pencil')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запускаю отрисовку для класса Handle')


st = Stationery('Кисточка')
print(st.title)
st.draw()

pn = Pen('Эрик Краузе')
print(pn.title)
pn.draw()

pl = Pencil('Карандашулик')
print(pl.title)
pl.draw()

hl = Handle('Маркер2000')
print(hl.title)
hl.draw()

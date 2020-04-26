# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание! Вы превысили допустимую скорость! Для вашего автомобиля она составляет 60 км/ч.')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')
        if self.speed > 40:
            print('Внимание! Вы превысили допустимую скорость! Для вашего автомобиля она составляет 40 км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t = TownCar(61, 'Зеленый', 'Ласточка', False)
print(t.speed, t.color, t.name, t.is_police)
t.go()
t.stop()
t.turn('направо')
t.show_speed()

w = WorkCar(45, 'Красный', 'Белочка', False)
print(w.speed, w.color, w.name, w.is_police)
w.go()
w.stop()
w.turn('налево')
w.show_speed()

p = PoliceCar(90, 'Белый', 'Фараон', True)
print(p.speed, p.color, p.name, p.is_police)
p.go()
p.stop()
p.turn('назад')
p.show_speed()

s = SportCar(150, 'Синий', 'Орлик', False)
print(s.speed, s.color, s.name, s.is_police)
s.go()
s.stop()
s.turn('направо')
s.show_speed()

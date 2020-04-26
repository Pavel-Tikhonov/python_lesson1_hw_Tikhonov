# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = 'Красный'

    def running(self, timer_red, timer_yellow, timer_green):
        self.timer_red = timer_red
        self.timer_yellow = timer_yellow
        self.timer_green = timer_green

        while True:
            try:
                print(TrafficLight.__color)
                sleep(timer_red)
                TrafficLight.__color = 'Желтый'
                print(TrafficLight.__color)
                sleep(timer_yellow)
                TrafficLight.__color = 'Зеленый'
                print(TrafficLight.__color)
                sleep(timer_green)
                TrafficLight.__color = 'Красный'
            except KeyboardInterrupt:
                print('Работа сфетофора окончена')
                break


tr = TrafficLight()
tr.running(7, 2, 5)

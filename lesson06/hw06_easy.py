# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
# о том что машина поехала, остановилась, повернула(куда)
 
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
    
    def get_speed(self):
        return self._speed
    
    def get_color(self):
        return self._color
    
    def get_name(self):
        return self._name

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print('Машина повернула {}'.format(direction))


class SportCar(TownCar):
    pass

class WorkCar(SportCar):
    pass

class PoliceCar(WorkCar):
    def __init__(self, speed, color, name, is_police=False):
        super(PoliceCar, self).__init__(self, speed, color, name, is_police=True)



car1 = WorkCar(80, 'blue', 'Audi')

print(car1.get_name(), car1.get_color(), car1.get_speed())
print(car1.go())
print(car1.stop())
print(car1.turn("направо"))

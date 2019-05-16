# coding: utf-8

import datetime
import math

__author__ = 'Тимофеев Алексей'

print("Список задач:")
print("[1] - Задача-1")
print("[2] - Задача-2")
print("[3] - Задача-3")

task = int(input("Какую задачу будем решать? "))

if task == 1:
    # Задача-1
    equation = 'y = -12x + 11111140.2121'
    x = 2.5
    k = int(equation[3:equation.find('x')])
    b = float(equation[equation.find('+') + 1:])
    print(k)
    print(b)
    y = k*x + b
    print(y)
elif task == 2:
    # Задача-2
    try:
        day = int(input('Введите день: '))
        month = int(input('Введите месяц: '))
        year = int(input('Введите год: '))
        data1 = datetime.date(year, month, day)
        print(data1)
    except ValueError:
        print('Введите корректную дату!')
elif task == 3:
    # Задача-3
    room = int(input("Введите номер комнаты: "))
    capacity = 0
    i = 0
    floor = 0
    while capacity < room:
        capacity1 = capacity
        capacity += i**2
        floor += i
        i += 1  
    lastsquarecapacity = capacity - capacity1
    floortop = math.ceil((room - capacity1)/(i - 1))
    floor = floor - (i - 1) + floortop
    place = room - capacity1 - (floortop - 1) * (i - 1)
    print (floor, place)


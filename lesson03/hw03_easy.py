# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def information(name, age, city):
    return ('{}, {} (а), проживает в городе {}'.format(name, age, city))

name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")
print(information(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(number1, number2, number3):
    return max(number1, number2, number3)

print(max_number(1, 6, 10))
 
# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def findlongest(*args):
    return max(list(map(str, args)), key=len)

print(findlongest(1, '5', '2314', 'sdf'))

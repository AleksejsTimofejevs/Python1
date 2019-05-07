# coding: utf-8

__author__ = 'Тимофеев Алексей'

print("Список задач:")
print("[1] - Задача-1")
print("[2] - Задача-2")
print("[3] - Задача-3")

task = int(input("Какую задачу будем решать? "))

if task == 1:
    # Задача-1
    fruits = ["яблоко", "банан", "киви", "арбуз"]
    for i in fruits:
        print(str(fruits.index(i) + 1) + ".", i.rjust(6))
elif task == 2:
    # Задача-2
    list1 = list(input("Введите 1 список через пробел: ").split())
    list2 = list(input("Введите 2 список через пробел: ").split())
    list3 = list1.copy()
    for i in list1:
        if i in list2:
            list3.pop(list3.index(i))
    list1.clear()
    list1 = list3.copy()    
    print(list1)
elif task == 3:
    # Задача-3
    list4 = list(map(int,input("Введите 1 список через пробел: ").split()))
    list5 = []
    for i in list4:
        if i%2 == 0:
            list5.append(i/4)
        else:
            list5.append(i*2)
    print(list5)
else:
    pass
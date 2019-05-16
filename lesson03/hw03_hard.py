# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
 
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

#Начальные данные
name1 = input("Введите имя игрока: ")
name2 = input("Введите имя врага: ")
player = {"name": name1, "health": 100, "damage": 15, "armor": 1.2}
enemy = {"name": name2, "health": 100, "damage": 20, "armor": 1.2}

#Запись начальных данных в файл
with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(player['name']+".txt"), "w") as file:
    for key,value in player.items():
        file.write("{} - {}\n".format(key, value))

with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(enemy['name']+".txt"), "w") as file:
    for key,value in enemy.items():
        file.write("{} - {}\n".format(key, value))


#Функция (Выгрузка информации из файлов и запись их в словари, нанесение удара, загрузка данных обратно в словари)
def attack(person1, person2):
    global pobeda
    pobeda = False
    person11 = person1
    person22 = person2
    #Выгрузка данных о 1 существе в словарь
    with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person1+".txt"), "r") as file:
        person1 = {"name": person1}
        for line in file:
            list1 = line.strip().split()
            person1[list1[0]] = list1[2]
    #Выгрузка данных о 2 существе в словарь
    with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person2+".txt"), "r") as file:
        person2 = {"name": person2}
        for line in file:
            list2 = line.strip().split()
            person2[list2[0]] = list2[2]

    #Проверка останется ли здоровье после удара
    if float(person2["health"]) < (float(person1["damage"])/float((person2["armor"]))):
        person2["health"] = 0
        print("Победил {}, осталось {} здоровья".format(person1["name"], person1["health"]))
        pobeda = True
    #Выгрузка данных после победного удара
        with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person11+".txt"), "w") as file:
            for key,value in person1.items():
                file.write("{} - {}\n".format(key, value))
        
        with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person22+".txt"), "w") as file:
            for key,value in person2.items():
                file.write("{} - {}\n".format(key, value))
    
    else:
        person2["health"] = float(person2["health"]) - float(person1["damage"])/float((person2["armor"]))

        with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person11+".txt"), "w") as file:
            for key,value in person1.items():
                file.write("{} - {}\n".format(key, value))
        
        with open('/Users/a1/Desktop/Python1/lesson03/{}'.format(person22+".txt"), "w") as file:
            for key,value in person2.items():
                file.write("{} - {}\n".format(key, value))

    print("{} атаковал {} и нанес ему {} урона!".format(person1["name"], person2["name"], float(person1["damage"])/float((person2["armor"]))))

#Сам бой

person1 = input("Введите имя 1 существа: ")
person2 = input("Введите имя 1 существа: ")
pobeda = False

while pobeda == False:
    attack(person1, person2)
    if pobeda == True:
        break
    attack(person2, person1)
    if pobeda == True:
        break
 
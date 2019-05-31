# coding: utf-8

__author__ = 'Тимофеев Алексей'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class Card:
    
    def createcard(self):
        name = random.sample(range(1, 91), 15)
        raw1 = name[slice(0,5)]
        raw2 = name[slice(5,10)]
        raw3 = name[slice(10,15)]
        for _ in range(5):
            raw1.append('')
            raw2.append('')
            raw3.append('')
        random.shuffle(raw1)
        random.shuffle(raw2)
        random.shuffle(raw3)
        name = [raw1, raw2, raw3]
        return name

    def printcard(self, name):
        print("-----------------------------------------------")
        for raw in name:
            print(raw)
        print("-----------------------------------------------")

class Game:

    #ход игры
    def bochki(self):
        list1 = random.sample(range(1, 91), 90)
        random.shuffle(list1)
        return list1
    
    def checkforcomputer(self, parametr, name):
        for raw in name:
            if parametr in raw:
                raw.insert(raw.index(parametr), "-")
                raw.remove(parametr)
        return name

    def crossforhuman(self, parametr, name):
        for raw in name:
            if parametr in raw:
                raw.insert(raw.index(parametr), "-")
                raw.remove(parametr)
        return name

    def checkifcross(self, parametr, name):
        result = False
        for raw in name:
            if parametr in raw:
                result = True
        return result
    

#Начало игры
card = Card()

#Создание и отображение карточек
player = card.createcard()
card.printcard(player)

computer = card.createcard()
card.printcard(computer)

game = Game()

#создание хода игры
list1 = game.bochki()
iforhuman = 0
iforcomputer = 0
k=1

for i in list1:
    print("Ход номер: ", k)
    k += 1
    print("Выпало число: ", i)
    card.printcard(player)
    card.printcard(computer)
    check = input("Зачеркнуть цифру? (y/n)?")
    if check == "y":
        if game.checkifcross(i, player) == True:
            game.crossforhuman(i, player)
            iforhuman += 1
        else:
            print("Вы проиграли!")
            raise SystemExit
    elif check == "n":
        if game.checkifcross(i, player) == True:
            print("Вы проиграли!")
            raise SystemExit
    else:
        print("Вы дали некорректный ответ! Вы проиграли!")
        raise SystemExit

    if game.checkifcross(i, computer) == True:
        iforcomputer +=1

    game.checkforcomputer(i, computer)

    if iforhuman == 15:
        print("Вы победили!")
        raise SystemExit
    
    if iforcomputer == 15:
        print("Победил компьютер!")
        raise SystemExit

print("Конец игры!")
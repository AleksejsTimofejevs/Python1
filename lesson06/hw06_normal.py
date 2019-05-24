# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
class Person:
    def __init__(self, name, health, damage, armor):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor
    
    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._health

    def get_damage(self):
        return self._damage
    
    def get_armor(self):
        return self._armor

    
class Player(Person):
    pass

class Enemy(Person):
    pass

class Fight:
    def __init__(self, creature1, creature2):
        self._creature1 = creature1
        self._creature2 = creature2
    
    def start(self, creature1, creature2):
        while creature1._health > 0 and creature2._health > 0:
            damageperhit = creature1._damage/creature2._armor
            creature2._health -= damageperhit
            if creature2._health <= 0:
                print('{} победил, осталось !'.format(creature1.name))
                break
            damageperhit = creature1._damage/creature2._armor
            creature2._health -= damageperhit
            if creature1._health <= 0:
                print('{} победил, осталось !'.format(creature2.name))


player = Player('Игрок1', 120, 40, 2)
enemy = Enemy('Игрок2', 200, 20, 3)

startfight = Fight(player, enemy)
startfight.start(player, enemy)
        
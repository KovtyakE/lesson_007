# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 70.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return '{}: сытость: {}'.format(self.name, self.fullness)

    def eat(self):
        if self.fullness <= 100:
            if self.house.food >= 10:
                cprint('{} поел'.format(self.name), color='yellow')
                self.fullness += 10
                self.house.food -= 10
            else:
                cprint('{}: нет еды'.format(self.name), color='red')
        else:
            cprint('{} не ел, потому что сыт'.format(self.name), color='yellow')
    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play_PC(self):
        cprint('{} играл за компом целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{}: на еду нет денег!'.format(self.name), color='red')

    def bring_cat_to_home(self, cat, house):
        self.cat = cat
        self.cat.house = house
        self.cat.fullness -= 10
        cprint('{} приютил котика по кличке {}'.format(self.name, self.cat.name), color='cyan')

    def cat_food_shopping(self):
        if self.house.money >= 70:
            cprint('{} сходил в магазин за едой для кошек'.format(self.name), color='magenta')
            self.house.money -= 70
            self.house.cat_food += 50
        else:
            cprint('{}: на еду для кошек денег не хватает!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} убрался в доме и переклеил обои'.format(self.name), color='green')
        self.house.dirty -= 100
        self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 70:
            self.work()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 40:
            self.cat_food_shopping()
        elif self.fullness >= 30 and self.house.dirty >= 100:
            self.clean_house()
        elif dice == 1 or dice == 3 or dice == 5:
            self.work()
        elif dice == 2:
            self.cat_food_shopping()
        elif dice == 4:
            self.shopping()
        else:
            self.play_PC()


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот {}: сытость: {}'.format(self.name, self.fullness)

    def eat(self):
        cprint('Кот {} поел'.format(self.name), color='yellow')
        self.fullness += 20
        self.house.cat_food -= 10

    def sleep(self):
        cprint('Кот {} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def make_some_dirt(self):
        cprint('Кот {} дерёт обои'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.dirty += 5

    def act(self):
        if self.fullness < 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 40 and self.house.cat_food >= 10:
            self.eat()
        elif dice == 1 and self.house.cat_food >= 10:
            self.eat()
        elif dice == 2 or dice == 3:
            self.make_some_dirt()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 0
        self.dirty = 0

    def __str__(self):
        return 'Состояние дома: \nЕда: {} \nДеньги: {} \nКошачий корм: {} \nБеспорядок: {}'.format(
            self.food, self.money, self.cat_food, self.dirty)


citizens = [Man(name='Василий')]
cats = [Cat(name='Васька'),
        Cat(name='Барсик'),
        Cat(name='Мурзик'),
        Cat(name='Снежок'),
        ]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
for cat in cats:
    citizens[0].bring_cat_to_home(cat=cat, house=my_sweet_home)

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.eat()
        citizen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)
    # input('Нажмите Enter для продолжения')

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

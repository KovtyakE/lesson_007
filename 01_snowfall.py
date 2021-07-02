# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

sd.set_screen_size(1500, 750)
sd.background_color = sd.COLOR_BLACK

N = 20
red = sd.COLOR_RED
orange = sd.COLOR_ORANGE
yellow = sd.COLOR_YELLOW
green = sd.COLOR_GREEN
cyan = sd.COLOR_CYAN
blue = sd.COLOR_BLUE
purple = sd.COLOR_PURPLE
color_list = [red, orange, yellow, green, cyan, blue, purple]
flakes_list = []
fallen_flakes_list_to_delete = []
lying_snowflakes = []


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.factor_a = randint(4, 8) / 10
        self.factor_b = randint(25, 45) / 100
        self.factor_c = randint(50, 70)
        self.coord_x = randint(100, 1400)
        self.coord_y = randint(750, 950)
        self.size = randint(15, 30)
        self.color = color_list[randint(0, 6)]
        self.missing_snowflakes_list = []

    def clear_previous_picture(self):
        sd.start_drawing()
        start_point = sd.get_point(self.coord_x, self.coord_y)
        sd.snowflake(start_point, length=self.size, color=sd.background_color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)
        sd.finish_drawing()

    def move(self):
        self.coord_x += randint(-2, 2)
        self.coord_y -= randint(3, 6)

    def draw(self):
        sd.start_drawing()
        start_point = sd.get_point(self.coord_x, self.coord_y)
        sd.snowflake(start_point, length=self.size, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)
        sd.finish_drawing()

    def can_fall(self):
        if self.coord_y < 30:
            return False
        else:
            return True


def one_snowflake_drawing():
    one_flake = Snowflake()

    while True:
        one_flake.clear_previous_picture()
        one_flake.move()
        one_flake.draw()
        if not one_flake.can_fall():
            break
        sd.sleep(0.03)
        if sd.user_want_exit():
            break


def get_alot_of_flakes():
    for flake_num in range(N):
        flake_from_lot = Snowflake()
        flakes_list.append(flake_from_lot)
    return flakes_list


def get_fallen_flakes():
    counter = 0
    if flake.coord_y < 80:
        counter += 1
        fallen_flakes_list_to_delete.append(flake)
    return counter


def append_flakes(count):
    for flake_num in range(count):
        flake_from_lot = Snowflake()
        flakes_list.append(flake_from_lot)
    return flakes_list


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_alot_of_flakes()  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подcчитать сколько снежинок уже упало
        if fallen_flakes:
            for fallen_flake in fallen_flakes_list_to_delete:
                lying_snowflakes.append(fallen_flake)
                flakes_list.remove(fallen_flake)
            fallen_flakes_list_to_delete.clear()
            append_flakes(count=fallen_flakes)  # добавить еще сверху
    for lying_snowflake in lying_snowflakes:
        lying_snowflake.draw()
        if len(lying_snowflakes) > 20:
            lying_snowflakes.pop(0)
    # sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

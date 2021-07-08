# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)


class Ground:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Water()) or str(element_2) == str(Water()):
            if str(element_1) == str(Air()) or str(element_2) == str(Air()):
                result = Storm()
                return result


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Water()) or str(element_2) == str(Water()):
            if str(element_1) == str(Fire()) or str(element_2) == str(Fire()):
                result = Steam()
                return result


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Water()) or str(element_2) == str(Water()):
            if str(element_1) == str(Ground()) or str(element_2) == str(Ground()):
                result = Dirt()
                return result


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Air()) or str(element_2) == str(Air()):
            if str(element_1) == str(Fire()) or str(element_2) == str(Fire()):
                result = Lightning()
                return result

class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Air()) or str(element_2) == str(Air()):
            if str(element_1) == str(Ground()) or str(element_2) == str(Ground()):
                result = Dust()
                return result


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        return Reaction(elem_1=self, elem_2=other)

    def is_right_reaction(element_1, element_2):
        if str(element_1) == str(Fire()) or str(element_2) == str(Fire()):
            if str(element_1) == str(Ground()) or str(element_2) == str(Ground()):
                result = Lava()
                return result


class Reaction:
    def __init__(self, elem_1, elem_2):
        self.elem_1 = elem_1
        self.elem_2 = elem_2
        self.result = self.which_reaction_is_there(self.elem_1, self.elem_2)


    def which_reaction_is_there(self, elem_1, elem_2):
        result = Storm.is_right_reaction(elem_1, elem_2)
        if result:
            return result
        result = Steam.is_right_reaction(elem_1, elem_2)
        if result:
            return result
        result = Dirt.is_right_reaction(elem_1, elem_2)
        if result:
            return result
        result = Lightning.is_right_reaction(elem_1, elem_2)
        if result:
            return result
        result = Dust.is_right_reaction(elem_1, elem_2)
        if result:
            return result
        result = Lava.is_right_reaction(elem_1, elem_2)
        if result:
            return result

    def __str__(self):
        return 'В результате реакции элементов: (' + str(self.elem_1) + ' + ' + str(self.elem_2) + ') образуется ' \
               + str(self.result)
    # Сложение элементов реализовывать через __add__



# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
print(Water() + Air())
print(Fire() + Water())
print(Ground() + Water())
print(Fire() + Air())
print(Fire() + Ground())
print(Ground() + Air())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

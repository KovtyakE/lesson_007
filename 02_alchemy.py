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

    def __add__(self, element_2):
        if str(element_2) == str(Air()):
            return Reaction(elem_1=self, elem_2=Air(), result=Storm())
        elif str(element_2) == str(Fire()):
            return Reaction(elem_1=self, elem_2=Fire(), result=Steam())
        elif str(element_2) == str(Ground()):
            return Reaction(elem_1=self, elem_2=Ground(), result=Dirt())
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, element_2):
        if str(element_2) == str(Water()):
            return Reaction(elem_1=self, elem_2=Water(), result=Storm())
        elif str(element_2) == str(Fire()):
            return Reaction(elem_1=self, elem_2=Fire(), result=Lightning())
        elif str(element_2) == str(Ground()):
            return Reaction(elem_1=self, elem_2=Ground(), result=Dust())
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, element_2):
        if str(element_2) == str(Air()):
            return Reaction(elem_1=self, elem_2=Air(), result=Lightning())
        elif str(element_2) == str(Water()):
            return Reaction(elem_1=self, elem_2=Water(), result=Steam())
        elif str(element_2) == str(Ground()):
            return Reaction(elem_1=self, elem_2=Ground(), result=Lava())
        else:
            return None


class Ground:
    def __str__(self):
        return 'Земля'

    def __add__(self, element_2):
        if str(element_2) == str(Air()):
            return Reaction(elem_1=self, elem_2=Air(), result=Dust())
        elif str(element_2) == str(Fire()):
            return Reaction(elem_1=self, elem_2=Fire(), result=Lava())
        elif str(element_2) == str(Water()):
            return Reaction(elem_1=self, elem_2=Water(), result=Dirt())
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'
# TODO попробовать реализовать через строку ниже метод is_right_reaction с неким циклом проверки всех условий

# if str(elem_1) == str(Water()) or str(elem_2) == str(Air()):
#     print(1)


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        pass


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        pass


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        pass


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        pass


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        pass


class Reaction:
    def __init__(self, elem_1, elem_2, result):
        self.elem_1 = elem_1
        self.elem_2 = elem_2
        self.result = result

        # if type(self.elem_1) or type(self.elem_2) == type(Water()):
        #     if type(self.elem_1) or type(self.elem_2) == type(Air()):
        #         self.reaction = Storm()
        #     elif type(self.elem_1) or type(self.elem_2) == type(Fire()):
        #         self.reaction = Steam()
        #     elif type(self.elem_1) or type(self.elem_2) == type(Ground()):
        #         self.reaction = Dirt()
        #     else:
        #         self.reaction = None

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
water = Water()
air = Air()
fire = Fire()

print(Ground() + Fire())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

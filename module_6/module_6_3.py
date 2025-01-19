# Домашнее задание по теме "Множественное наследование"
#
# Ваша задача:
#
# Цель: закрепить знания множественного наследования в Python.
#
# Задача "Ошибка эволюции":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами?
# Например, утконос ... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах.
# А ещё он откладывает яйца ... Опустим тот факт, что они потеют молоком, и попробуем
# не эволюционным способом создать нашего утконоса.
# Необходимо написать 5 классов:
#
# Animal - класс описывающий животных.
# Класс обладает следующими атрибутами:
#     1. live = True
#     2. sound = None - звук (изначально отсутствует)
#     3. _DEGREE_OF_DANGER = 0 - степень опасности существа
# Объект этого класса обладает следующими атрибутами:
#     1. _coordinates = [0, 0, 0] - координаты в пространстве.
#     2. speed = ... - скорость передвижения существа (определяется при создании объекта)
# И методами:
#     1. move(self, dx, dy, dz), который должен менять соответствующие координаты в _coordinates на dx, dy и dz
#        в том же порядке, где множителем будет являться speed. Если при попытке изменения координаты z в _coordinates
#        значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(",
#        при этом изменения не вносятся.
#     2. get_coordinates(self), который выводит координаты в формате:
#        "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
#     3. attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
#        "Be careful, i'm attacking you 0_0", если равно или больше.
#     4. speak(self), который выводит строку со звуком sound.
#
# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
#     1. beak = True - наличие клюва
# И методом:
#     1. lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
#
# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 3.
# Должен обладать методом:
#     1. dive_in(self, dz) - где dz изменение координаты z в _coordinates. Этот метод должен всегда уменьшать
#        координату z в _coordinates. Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
#        Скорость движения при нырянии должна уменьшаться в 2 раза, в отличие от обычного движения. (speed / 2)
#
# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 8.
#
# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
#     1. sound = "Click-click-click" - звук, который издаёт утконос
#
# Пример результата выполнения программы:
# Пример работы программы:
#
# db = Duckbill(10)
#
# print(db.live)
# print(db.beak)
#
# db.speak()
# db.attack()
#
# db.move(1, 2, 3)
# db.get_coordinates()
# db.dive_in(6)
# db.get_coordinates()
#
# db.lay_eggs()
#
# Вывод на консоль:
#
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you # Число может быть другим (1-4)
#
# По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.
# После чего утконос совершает манёвры и ныряет.
# Теперь утконос в безопасности, он откладывает яйца для будущего потомства.
#
# Примечания:
#     1. Будьте внимательней, когда вызываете методы классов родителей в классе-наследнике
#        при множественном наследовании: при обращении через super() методы будут искаться сначала
#        в первом, потом во втором и т.д. классах по mro().
#     2. При определении порядка наследования обратите внимание на то, что утконос атакует
#        "Be careful, i'm attacking you 0_0".

import random


class Animal:
    live = True
    sound = None  # звук, изначально отсутствует
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._coordinates = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        saved_coordinates = self._coordinates
        self._coordinates[0] += dx * self.speed
        self._coordinates[1] += dy * self.speed
        self._coordinates[2] += dz * self.speed
        if self._coordinates[2] < 0:
            print(f"It's too deep, i can't dive :(")
            self._coordinates = saved_coordinates

    def get_coordinates(self):
        print(f'X: {self._coordinates[0]}, Y: {self._coordinates[1]}, Z: {self._coordinates[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed = int(self.speed / 2)
        self._coordinates[2] -= abs(dz) * self.speed


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


if __name__ == '__main__':
    db = Duckbill(10)
    # print(Duckbill.mro())
    # print(db._DEGREE_OF_DANGER)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_coordinates()
    db.dive_in(6)
    db.get_coordinates()

    db.lay_eggs()

# Вывод на консоль:
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you # Число может быть другим (1-4)

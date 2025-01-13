# Задача "Developer - не только разработчик":
#
# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
#
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
#
# Пункты задачи:
#     1. Создайте класс House.
#     2. Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
#     3. Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
#     4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
#     5. Создайте объект класса House с произвольным названием и количеством этажей.
#     6. Вызовите метод go_to у этого объекта с произвольным числом.

import time

class House:

    def __init__(self, name, number_of_floors):
        self.name = name                            # название строения
        self.number_of_floors = number_of_floors    # количество этажей

    def go_to(self, new_floor):
        print(f'\nСтроение: {self.name}')

        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа ({new_floor}) не существует')
            return

        if new_floor == 1:
            print('Мы и так на первом этаже. Зачем куда-то идти?')

        elif self.number_of_floors <= 5:
            print('Лифта нет. Пойдем пешком.')
            for i in range(new_floor):
                time.sleep(2.0)
                print(i + 1)
            print(f'Уф-ф-ф! Мы на {new_floor} этаже')
        elif self.number_of_floors > 5:
            print('Лифт. Осторожно! Двери закрываются.')
            for i in range(new_floor):
                time.sleep(1.0)
                print(i + 1)
            print(f'Лифт на {new_floor} этаже')
        else:
            print('Как мы здесь оказались? Этого не может быть!')


troyka = House('ЖК "Тройка"', 23)
khrushchevka = House('Пятиэтажка', 5)
grandmas_hut = House('Бабушкина мазанка', 1)
pumpkin_hut = House('Хижина Тыквы', 0)
catacomb = House('Hell', -666)

troyka.go_to(-1)
troyka.go_to(0)
troyka.go_to(1)
troyka.go_to(5)
troyka.go_to(75)

grandmas_hut.go_to(0)
grandmas_hut.go_to(1)
grandmas_hut.go_to(2)

khrushchevka.go_to(0)
khrushchevka.go_to(3)
khrushchevka.go_to(6)

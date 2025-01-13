# "Специальные методы классов"
# Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
#
# Необходимо дополнить класс House следующими специальными методами:
#     __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#     __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20

import time

class House:

    def __init__(self, name, number_of_floors):
        self.name = name                            # название строения
        self.number_of_floors = number_of_floors    # количество этажей


    def __len__(self):
        return abs(self.number_of_floors)


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


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

for building in troyka, khrushchevka, grandmas_hut, pumpkin_hut, catacomb:
    print(building)

for building in troyka, khrushchevka, grandmas_hut, pumpkin_hut, catacomb:
    print(len(building))


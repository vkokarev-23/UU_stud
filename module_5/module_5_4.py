# Домашняя работа по уроку "Различие атрибутов класса и экземпляра".
#
# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс.
# Применить метод __new__.
#
# Дополнительно о работе метода __new__:
# Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
# Разберёмся, как происходит передача данных между ними на следующем примере:
# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#       print(first)
#       print(second)
#       print(third)
#
# ex = Example('data', second=25, third=3.14)
#
# Работа __new__:
#     1.'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент.
#        Он будет находиться под индексом 0 как единственный элемент кортежа.
#     2. second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы.
#        Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
#
# Передача данных из __new__ в __init__:
# После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
#     1. В параметр first распакуется из args единственный аргумент 'data'.
#     2. В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
#     3. В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
#
# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться
# к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
#     1. Название объекта добавлялось в список cls.houses_history.
#     2. Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.
#
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# # Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
#
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
#
# Примечания:
#     1. Более подробно о работе метода __new__ можно узнать здесь.
#     2. В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.
#
# Файл module_5_4.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.


import time

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        # print(f'args: {args}')
        # print(f'kwargs: {kwargs}')
        cls.houses_history.append(args[0])
        # print(f'houses_history: {cls.houses_history}')
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name                            # название строения
        self.number_of_floors = number_of_floors    # количество этажей


    def __len__(self):
        return abs(self.number_of_floors)


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self


    def __radd__(self, other):
        return self.__add__(other)


    def __iadd__(self, other):
        return self.__add__(other)


    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')


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


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

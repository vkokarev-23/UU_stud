# Домашнее задание по теме "Режимы открытия файлов"
#
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
#
# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vegetables') и обладать
# следующими свойствами:
#     1. Атрибут name - название продукта (строка).
#     2. Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
#     3. Атрибут category - категория товара (строка).
#     4. Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
#        Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
#     1. Инкапсулированный атрибут __file_name = 'products.txt'.
#     2. Метод get_products(self), который считывает всю информацию из файла __file_name,
#        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
#     3. Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
#        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
#        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
#
# Пример результата выполнения программы:
# Пример работы программы:
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(p2) # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
#
#     Вывод на консоль:
#     Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
#     Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
# Как выглядит файл после запусков (смотрите файл домашнего задания)
#
# Примечания:
#     1. Не забывайте при записи в файл добавлять спецсимвол перехода на следующую строку в конце - '\n'.
#     2. При проверке на существование товара в методе add можно вызывать метод get_products
#        для получения текущих продуктов.
#     3. Не забывайте закрывать файл вызывая метод close() у объектов файла.

import os
from itertools import chain


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'

    def __iter__(self):
        return iter([self.name, self.weight, self.category])

    def __next__(self):
        pass


class Shop:
    __file_name = 'products.txt'

    def print_products_from_file(self):
        fd = open(self.__file_name, 'r')
        for line in fd:
            print(line, end="")
        fd.close()

    def products_from_file(self):
        if not os.path.isfile(self.__file_name):
            return
        fd = open(self.__file_name, 'r', newline='')
        for line in fd:
            name, weight, category = line.splitlines()[0].split(sep=',')
            yield name, weight, category
        fd.close()

    def products_from_adds(self, *products):
        for prod in products:
            name, weight, category = str(prod).split(sep=',')
            yield name, weight, category

    def print_all_products(self, *products):
        for prod in chain(self.products_from_file(), self.products_from_adds(*products)):
            print(prod)

    def save_dict_to_file(self, d_prod):
        fd = open(self.__file_name, 'wt')
        for prod in d_prod:
            print(f'{prod},{d_prod[prod][0]},{d_prod[prod][1]}', file=fd)
        fd.close()

    def update_products(self, *products):
        dict_prod = dict()
        for prod in chain(self.products_from_file(), self.products_from_adds(*products)):
            name = prod[0]
            weight = prod[1]
            category = prod[2]
            if dict_prod.get(name):
                print(f'Продукт {name} уже есть в магазине')
            else:
                dict_prod[name] = weight, category
        self.save_dict_to_file(dict_prod)

    def make_products_file(self, *products):
        fd = open(self.__file_name, 'wt')
        for prod in products:
            print(prod, file=fd)
        fd.close()

#========================================================================================================
    # Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
    # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
    def add(self, *products):
        self.update_products(*products)


    # Метод get_products(self), который считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами.
    def get_products(self):
        fd = open(self.__file_name, 'r')
        all_products = fd.read()
        fd.close()
        return all_products


# Пример работы программы:
if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato_1', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato_2', 5.5, 'Vegetables')

    print(p2, '\n') # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

#     Вывод на консоль:
#     Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
#     Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

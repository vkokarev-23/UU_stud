# Организация программ и методы строк

# 1.  Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
my_string = input("введите текст: ")
print ("my_string =", "'" + my_string + "'", type(my_string))

# 2.  Вывести количество символов введённого текста
print ("length my_string =", len(my_string))

# 3. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
#
# 3.1    Выведите строку my_string в верхнем регистре.
print ("upper my_string =", my_string.upper())

# 3.2    Выведите строку my_string в нижнем регистре.
print ("lower my_string =", my_string.lower())

# 3.3    Измените строку my_string, удалив все пробелы.
print ("kill spaces my_string =", my_string.replace (" ", ""))

# 3.4    Выведите первый символ строки my_string.
print ("first char my_string =", my_string[0])

# 3.5    Выведите последний символ строки my_string.
print ("last char my_string =", my_string[-1])

# пункты 3.4 и 3.5 - это не методы, а срезы, но так проще

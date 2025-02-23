# Распаковка позиционных параметров
#
# 1. Функция с параметрами по умолчанию:
#
#     1.1 Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает
#         три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
#     1.2 Функция должна выводить эти параметры.
#     1.3 Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#     1.4 Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
#
# 2. Распаковка параметров:
#
#     2.1 Создайте список values_list с тремя элементами разных типов.
#     2.2 Создайте словарь values_dict с тремя ключами, соответствующими параметрам
#         функции print_params, и значениями разных типов.
#     2.3 Передайте values_list и values_dict в функцию print_params,
#         используя распаковку параметров (* для списка и ** для словаря).
#
# 3. Распаковка + отдельные параметры:
#
#     3.1 Создайте список values_list_2 с двумя элементами разных типов
#     3.2 Проверьте, работает ли print_params(*values_list_2, 42)


def print_params(a=1, b='строка', c=True):
    print(f'print_params: {a = }  {b = }  {c = }')


print('\n1. Функция с параметрами по умолчанию:')
print_params(3, 5, 7)
print_params(b=5, c=7, a=3)
print_params(b=5, c=7)
print_params(c=7)
print_params(b=5)
print_params(a=3)
print_params()
print()
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n2. Распаковка параметров:')
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print('\n   Список')
print_params(values_list)  # как первый позиционный
print_params(*values_list)  # правильная распаковка
# print_params(**values_list)   # ОШИБКА: argument after ** must be a mapping, not list

print('\n   Словарь')
print_params(values_dict)  # как первый позиционный
print_params(*values_dict)  # распаковались значения ключей. Не пропускай звездочки!
print_params(**values_dict)  # правильная распаковка

print('\n3. Распаковка + отдельные параметры:')
values_list_2 = [1, 'строка']
print_params(*values_list_2, 42)  # работает
# print_params(*values_list_2, с = 42)    # ОШИБКА: нельзя именованные после распаковки
# print_params(a = 42, *values_list_2)    # ОШИБКА: got multiple values for argument 'a'
# print_params(b = 42, *values_list_2)    # ОШИБКА: got multiple values for argument 'b'
# print_params(с = 42, *values_list_2)    # ОШИБКА: got an unexpected keyword argument 'с'
print_params(42, *values_list_2)  # работает

print()
print('1. ', dir(print_params))
print('2. ', getattr(print_params, '__defaults__'))
print('3. ', print_params.__defaults__[0])

for attr_name in dir(range):
    attr_value = getattr(range, attr_name)
    print(f"{attr_name}: {attr_value}")

print()


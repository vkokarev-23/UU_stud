# Дополнительное практическое задание по модулю: "Подробнее о функциях."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
#
# Наши студенты, без исключения,- очень умные ребята. Настолько умные, что иногда по утру сами путаются в том,
# что намудрили вчера вечером. Один из таких учеников уснул на клавиатуре в процессе упорной учёбы
# (ещё и трудолюбивые). Тем не менее даже после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и
# длин всех строк?" Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре
# (списку, словарю и т.д.) по-разному. Ученику пришлось каждый раз использовать индексацию и обращение
# по ключам - универсального решения для таких структур он не нашёл.
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
#     Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#     Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
#
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):
#     1. Весь подсчёт должен выполняться одним вызовом функции.
#     2. Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
#     3. Так как каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
#     4. Для определения типа данного используйте функцию isinstance.


# Цитата.
# Ключи Python должны быть неизменяемыми типами данных — например, строками, числами или кортежами.
# Если сделать ключом список, словарь или другой изменяемый тип данных, возникнет ошибка.
# А вот значения словаря Python могут быть абсолютно любыми, в том числе и другими словарями.

# Замечание.
# Вариант, когда ключом в словаре выступает кортеж, в примере не отражен.

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum_1(dt_structure, total=0):

    match dt_structure:
        case int(x) | float(x):
            total += x
            print(f"digit {x = }  {total = }")
        case str(x):
            total += len(x)
            print(f"str   {x = }  len={len(x)}  {total = }")
        case list(x) | tuple(x) | set(x):
            print(f"iter  {x = }")
            for item in x:
                total = calculate_structure_sum_1(item, total)
        case dict(x):
            print(f"dict  {x = }")
            for item in dict(x).keys():
                total = calculate_structure_sum_1(item, total)
            for item in dict(x).values():
                total = calculate_structure_sum_1(item, total)
        case _:
            print(f"Could be anything else {type(data_structure)}")

    return total


def calculate_structure_sum_2(dt_structure, total=0):

    if isinstance(dt_structure, (int, float)):
        total += dt_structure
    elif isinstance(dt_structure, str):
        total += len(dt_structure)
    elif isinstance(dt_structure, (list, tuple, set)):
        for item in dt_structure:
            total = calculate_structure_sum_2(item, total)
    elif isinstance(dt_structure, dict):
        for item in dt_structure.keys():
            total = calculate_structure_sum_2(item, total)
        for item in dt_structure.values():
            total = calculate_structure_sum_2(item, total)

    return total


result = calculate_structure_sum_1(data_structure)
print('\n\ncalculate_structure_sum_1')
print(f'{result = }')

result = calculate_structure_sum_2(data_structure)
print('\n\ncalculate_structure_sum_2')
print(f'{result = }')
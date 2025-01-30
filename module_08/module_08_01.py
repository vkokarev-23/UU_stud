# Домашнее задание по уроку "Try и Except".
#
# Задание "Программистам всё можно":
# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем
# сложить число(int) и строку(str)? Давайте исправим это недоразумение!
#
# Реализуйте следующую функцию:
#     1. add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление
# этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
#
# Пример кода:
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))
#
# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
#
# Примечания:
#     1. Конструкции try-except в функции выполняют строго ту обработку,
#        которая написана в задании (обращайте на важность порядка передачи данных).
#     2. Если хотите дополнить функции своими исключениями или написать отдельно
#        дополнительно собственные функции - это не запрещено, мы не против, чтобы вы
#        больше экспериментировали. Но в первую очередь выполните поставленную задачу.

def add_everything_up(a, b):
    debug = False
    # debug = True

    try:
        c = a + b
    except TypeError as ter:
        if debug:
            print(f'\nВ параметрах ошибка: "{a}" и "{b}"! {ter}')
        c = str(a) + str(b)
    except Exception as eee:
        print(eee)
    else:
        if debug:
            print(f'\nПараметры в норме: "{a}" и "{b}"')
    finally:
        pass

    return c


if __name__ == '__main__':

    debug = False
    debug = True

    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

    if debug:
        print()
        print(add_everything_up(123, None))
        print(add_everything_up(123, (1, 2, 3)))
        print(add_everything_up(123, [1, 2, 3]))
        print(add_everything_up(123, {1, 2, 3}))
        print(add_everything_up(123, {1:100, 2:200, 3:300}))

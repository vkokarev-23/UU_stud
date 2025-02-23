# Задача "Счётчик вызовов":
#
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
#
# Давайте реализуем данную фишку самостоятельно!
#
#
# Вам необходимо написать 3 функции:
#
#     1. Функция count_calls подсчитывающая вызовы остальных функций.
#     2. Функция string_info принимает аргумент - строку и возвращает кортеж из: длины
#        этой строки, строку в верхнем регистре, строку в нижнем регистре.
#     3. Функция is_contains принимает два аргумента: строку и список, и возвращает
#        True, если строка находится в этом списке,
#        False - если отсутствует.
#        Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#
# Пункты задачи:
#
#     1. Создать переменную calls = 0 вне функций.
#     2. Создать функцию count_calls и изменять в ней значение переменной calls.
#        Эта функция должна вызываться в остальных двух функциях.
#     3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
#     4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
#     5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
#     6. Вывести значение переменной calls на экран(в консоль).

from random import randint

# счетчик вызовов функций, один на все случаи
calls = 0

# список слов
list_words = []


def count_calls():
    global calls
    calls += 1


def string_info(word):
    count_calls()

    if not type(word) == str:
        return 0, '', ''

    return len(word), word.upper(), word.lower()


def is_contains(string, list_to_search):
    count_calls()

    if not type(string) == str:
        return False
    if not type(list_to_search) == list:
        return False

    str_up = str(string).upper()
    for wrd in list_to_search:
        if str_up == str(wrd).upper():
            return True
    return False


def init_random_word():
    global list_words

    big_text = "Область видимости или scope определяет контекст переменной, в рамках которого ее можно \
использовать. В Python есть два типа контекста: глобальный и локальный. \
Глобальный контекст. \
Глобальный контекст подразумевает, что переменная является глобальной, она определена вне \
любой из функций и доступна любой функции в программе. \
Локальный контекст. \
В отличие от глобальных переменных локальная переменная определяется внутри функции \
и доступна только из этой функции, то есть имеет локальную область видимости."

    s = big_text.replace('.', ' ')
    s = s.replace(',', ' ')
    list_words = s.split()
    for wrd in list_words:
        if len(wrd) < 3:
            list_words.remove(wrd)


def random_word():
    global list_words

    min_word = 0
    max_word = len(list_words) - 1
    return list_words[randint(min_word, max_word)]


# ===========================
init_random_word()

# формируем маленький список слов, которые будем проверять по большому списку
wrd_list = []
for i in range(5):
    wrd_list.append(random_word())
# добавим "кривых" слов
wrd_list.append('ЛокальНый')
wrd_list.append('пеРемеННых')
wrd_list.append('оБласт')
print(f"\n{wrd_list = }\n")

for wrd in wrd_list:
    print(f"string_info: проверяем {wrd = }")
    print(string_info(wrd))
    print(f"{calls = }\n")

for wrd in wrd_list:
    print(f"is_contains: проверяем {wrd = }")
    if is_contains(wrd, list_words):
        print(f"{wrd = } есть в списке")
    else:
        print(f"{wrd = } в списке НЕТ")
    print(f"{calls = }\n")

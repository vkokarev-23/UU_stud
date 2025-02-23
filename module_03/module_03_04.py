# Задача "Однокоренные":
#
# Напишите функцию single_root_words, которая принимает одно обязательное слово
# в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
#
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот, root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.
#
# Пункты задачи:
#     1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
#     2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
#     3. При помощи цикла for переберите предполагаемо подходящие слова.
#     4. Пропишите корректное относительно задачи условие, при котором добавляются слова
#        в результирующий список same_words.
#     5. После цикла верните образованный функцией список same_words.
#     6. Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.


def single_root_words(root_word, *other_words):
    word_1 = str(root_word).upper()
    same_words = []
    for wrd in range(len(other_words)):
        word_2 = str(other_words[wrd]).upper()
        if word_1 in word_2 or word_2 in word_1:
            same_words.append(other_words[wrd])
    return same_words


words = single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'riches')
print(f"\n1. pattern = 'rich'")
print(f"1. list = 'richest', 'orichalcum', 'cheers', 'riches'")
print(f"1. {words = }")

words = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f"\n2. pattern = 'Disablement'")
print(f"2. list = 'Able', 'Mable', 'Disable', 'Bagel'")
print(f"2. {words = }")

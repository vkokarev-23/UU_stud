# Домашнее задание по теме: Оператор "with"
#
# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
#
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и
# записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
#     1. 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
#     2. ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
#
# Алгоритм получения словаря такого вида в методе get_all_words:
#    1. Создайте пустой словарь all_words.
#    2. Переберите названия файлов и открывайте каждый из них, используя оператор with.
#    3. Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
#    4. Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке
#       (тире обособлено пробелами, это не дефис в слове).
#    5. Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
#    6. В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words
# для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов)
# можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
# # Логика методов find или count
#
# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
# It's a text for task Найти везде.
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text
#
# Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
#
# Запустите этот код с другими примерами предложенными здесь.
# Если решение верное, то результаты должны совпадать с предложенными.
#
# Примечания:
#     1. Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
#     2. Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).


class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)
        self.all_words = dict()


    # get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, mode='r', encoding='utf-8') as fd:
                all_txt = fd.read()
                symbols_to_remove = "\r\n.,;:!?-=—‘"
                for symbol in symbols_to_remove:
                    all_txt = all_txt.replace(symbol, " ")
                all_txt = all_txt.replace('    ', ' ')
                all_txt = all_txt.replace('   ', ' ')
                all_txt = all_txt.replace('  ', ' ')
                all_txt = all_txt.lower()
                all_wrd = all_txt.split(sep=' ')
                all_wrd = [i for i in all_wrd if i]     # удаляет пустые строки
                all_wrd = [i for i in all_wrd if i != '’']     # удаляет одиночный '’'

            self.all_words[file_name] = all_wrd
        return self.all_words


    # find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    def find(self, sample):
        sample = str(sample).lower()
        result = dict()
        for name, words in self.get_all_words().items():
            pos_sample = None
            for num in range(len(words)):
                if words[num] == sample:
                    pos_sample = num + 1
                    break
            result[name] = sample, pos_sample
        return result


    # count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.
    def count(self, sample):
        sample = str(sample).lower()
        result = dict()
        for name, words in self.get_all_words().items():
            num_sample = list(words).count(sample)
            result[name] = sample, num_sample
        return result


if __name__ == '__main__':

    wf = WordsFinder(
        'Mother Goose - Monday’s Child.txt',
        'Rudyard Kipling - If.txt',
        'Walt Whitman - O Captain! My Captain!.txt'    )

    wf.get_all_words()

    f1 = wf.find('Child')
    f2 = wf.find('you')
    f3 = wf.find('Rudyard')
    f4 = wf.find('Kipling')
    f5 = wf.find('dead')
    f6 = wf.find('Walt')
    f7 = wf.find('Whitman')
    f8 = wf.find('gay')

    c1 = wf.count('Child')
    c2 = wf.count('you')
    c3 = wf.count('Rudyard')
    c4 = wf.count('Kipling')
    c5 = wf.count('dead')
    c6 = wf.count('Walt')
    c7 = wf.count('Whitman')
    c8 = wf.count('gay')

    pass

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))     # 3 слово по счёту
    print(finder2.count('teXT'))    # 4 слова teXT в тексте всего

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

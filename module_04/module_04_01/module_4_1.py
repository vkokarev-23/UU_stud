# Задача "А как делить?":
#
# В школе нам говорили, что на 0 делить нельзя. Высшая же математика опровергает это и говорит,
# что результат при делении на 0 будет стремиться к бесконечности.
# Давайте реализуем оба способа, чтобы у вас всегда был выбор!
# Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
# В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)
#
# Пункты задачи:
#
#     1. Создайте модули fake_math и true_math.
#     2. Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
#     3. Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide
#        из модулей fake_math и true_math, назвав их разными именами на своё усмотрение,
#        чтобы не было конфликтов имён, при помощи оператора as.
#     4. Запустите эти функции в модуле module_4_1, передав первым аргументом
#        произвольное число отличное от 0, вторым аргументом - 0
#     5. Выведи результаты вызовов этих функций на экран(в консоль).
#
# Пример результата выполнения программы. Исходный код (названия функций могут быть другими):
#
# result1 = fake_divide(69, 3)
# result2 = fake_divide(3, 0)
# result3 = true_divide(49, 7)
# result4 = true_divide(15, 0)
#
# print(result1)
# print(result2)
# print(result3)
# print(result4)

# Вывод на консоль:
# 23.0
# Ошибка
# 7.0
# inf


from fake_math import divide as fake_divide
from true_math import divide as true_divide


print(fake_divide(69, 3))
print(fake_divide(3, 0))
print(true_divide(49, 7))
print(true_divide(15, 0))
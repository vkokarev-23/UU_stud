
# Стиль кода часть II. Цикл While
#
# Задача "Нули ничто, отрицание недопустимо!":
#
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное
# или не закончится список (выход за границу).
#
# Пункты задачи:
#
#     1.Запишите исходный список в переменную my_list.
#     2.Напишите цикл while с соответствующими задаче условиями.
#     3.Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_len = len(my_list)


print()
print("Вариант-1 бесконечный цикл")
i = 0
while True:
    if i >= list_len:
        print("Список закончился. Выход по 'break' ")
        break

    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        print("Выход 'break' по условию")
        print(f"Отрицательное число my_list[{i}] = {my_list[i]}")
        break
    i += 1


print()
print("Вариант-2 цикл с условием")
i = 0
while i < list_len:
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        print("Выход 'break' по условию")
        print(f"Отрицательное число my_list[{i}] = {my_list[i]}")
        break
    i += 1


print()
print("Вариант-3 цикл с условием без 'break' ")
i = 0
while i < list_len and my_list[i] >= 0:
    if my_list[i] > 0:
        print(my_list[i])
    i += 1


print()
print("Вариант-4 цикл 'for'  немного не в тему")
for ML in my_list:
    if ML > 0:
        print(ML)
    elif ML < 0:
        break

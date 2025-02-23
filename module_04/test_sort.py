from sorting.mode import *

data_0 = list(map(int, (input('Введите числа через пробел: ').split())))
data_1 = list(data_0)
data_2 = list(data_0)
data_3 = list(data_0)


# nn = bubble_sort_1(data_1)
# print(nn)
# print(data_1)
#
# nn = bubble_sort_2(data_2)
# print(nn)
# print(data_2)



n1 = bubble_sort_1(data_1)
n2 = selection_sort_1(data_2)
n3 = insertion_sort_1(data_3)

print('Пузырьковая сортировка: ', n1, data_1)
print('Сортировка выбором:     ', n2, data_2)
print('Сортировка вставкой:    ', n3, data_3)


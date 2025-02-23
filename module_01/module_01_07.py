
# На вход даны следующие данные:
#
#     Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#     Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# students <class 'set'> неупорядоченная последовательность
# выдает элементы, в т.ч. на печать, в случайном порядке
# чтобы упорядочить, преобразуем в список (list) и сортируем

stud_list = list(students)
stud_list.sort()

stud_dict = {}
i = 0
for stud_name in stud_list:
    sum = 0
    for grad in grades[i]:
        sum += grad
    average = sum / len(grades[i])
    print( i + 1, stud_name, grades[i], "average:", average )

    stud_dict[stud_name] = average
    i += 1

print()
print( stud_dict )

# 1 Aaron [5, 3, 3, 5, 4] average: 4.0
# 2 Bilbo [2, 2, 2, 3] average: 2.25
# 3 Johnny [4, 5, 5, 2] average: 4.0
# 4 Khendrik [4, 4, 3] average: 3.6666666666666665
# 5 Steve [5, 5, 5, 4, 5] average: 4.8

# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

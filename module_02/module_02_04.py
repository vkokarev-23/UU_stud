# Задача "Всё не так уж просто":
#
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# Используя этот список составьте второй список primes содержащий только простые числа.
#
# А так же третий список not_primes, содержащий все не простые числа.
#
# Выведите списки primes и not_primes на экран(в консоль).
#
# Пункты задачи:
#
#     1. Создайте пустые списки primes и not_primes.
#     2. При помощи цикла for переберите список numbers.
#     3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
#     4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
#     5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
#     в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
#     6. Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

print("\n  Вариант 1.")

for i in range(1, len(numbers)):
    yes_prime = True
    for k in range(1, i):
        if numbers[i] % numbers[k] == 0:
            yes_prime = False
            break
#    print(f"{numbers[i] = } {yes_prime}")
    if yes_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(f"{numbers = }")
print("\n  Ответ:")
print(f"{primes = }")
print(f"{not_primes = }")



print("\n\n  Вариант 2. Множества")

def is_prime(number):
    ''' возвращает True, если number - простое число '''
    middle = number // 2 + 1
    result = True
    if number == 1:
        result = False
    for divider in range(2, middle):
        if number % divider == 0:
            result = False
    return result


# сначала найдем множество простых делителей dividers
dividers = set()
middle = len(numbers) // 2
for i in range(middle):
    if is_prime(numbers[i]):
        dividers.add(numbers[i])
print(f"{numbers =}")
print(f"{dividers =}")

set_primes = set(numbers)
set_primes = set_primes - {1}
#print(f"{set_primes = }")

# а теперь для всех делителей повычеркиваем подмножества кратных и получим множество простых
for div in dividers:
    set_multiple = {i for i in range(div * 2, len(numbers) + 1, div)}
    set_primes = set_primes - set_multiple
#    print(f"{set_multiple = }")
#    print(f"{set_primes = }")

# теперь получим множество непростых (кратных) как дополнение
set_not_primes = set(numbers)
set_not_primes = set_not_primes - {1}
set_not_primes = set_not_primes - set_primes
#print()
#print(f"{set_primes = }")
#print(f"{set_not_primes = }")

# требуется вывести списки - сделаем и отсортируем
primes = list(set_primes)
not_primes = list(set_not_primes)
primes.sort()
not_primes.sort()
print('\n  Ответ:')
print(f"{primes = }")
print(f"{not_primes = }")

# Получилось замысловато, зато со множествами поработал

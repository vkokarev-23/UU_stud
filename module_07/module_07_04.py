# Домашнее задание по теме "Форматирование строк".
#
# Цель задания:
#     1. Освоить различные методы форматирования строк в Python.
#     2. Научиться применять эти методы в контексте описания соревнования.
#        История: соперничество двух команд - Мастера кода и Волшебники данных.
#
# Задание:
#     1. Создайте новый проект или продолжите работу в текущем проекте.
#     2. Напишите код, который форматирует строки для следующих сценариев.
#     3. Укажите переменные, которые должны быть вставлены в каждую строку.
#
# Использование %:
#     1. Переменные: количество участников первой команды (team1_num).
#     2. Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
#     1. Переменные: количество участников в обеих командах (team1_num, team2_num).
#     2. Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
#
# Использование format():
#     1. Переменные: количество задач решённых командой 2 (score_2).
#     2. Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
#     1. Переменные: время за которое команда 2 решила задачи (team1_time).
#     2. Пример итоговой строки: "Волшебники данных решили задачи за 18015.2 с !"
#
# Использование f-строк:
#     1. Переменные: количество решённых задач по командам: score_1, score_2
#     2. Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
#     1. Переменные: исход соревнования (challenge_result).
#     2. Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
#     1. Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
#     2. Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
#
# Комментарии к заданию:
#     1. В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
#     2. Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.
#        Например, для challenge_result:
#
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
#     result = ‘Победа команды Мастера кода!’
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
#     result = ‘Победа команды Волшебники Данных!’
# else:
#     result = ‘Ничья!’



# Пример входных данных

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
#     1. Переменные: количество участников первой команды (team1_num).
#     2. Пример итоговой строки: "В команде Мастера кода участников: 5 ! "

print("В команде Мастера кода участников: %d !" % team1_num)

#     1. Переменные: количество участников в обеих командах (team1_num, team2_num).
#     2. Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format():
#     1. Переменные: количество задач, решённых командой, 2 (score_2).
#     2. Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"

print("Команда Волшебники данных решила задач: {} !".format(score_2))

#     1. Переменные: время за которое команда 2 решила задачи (team1_time).
#     2. Пример итоговой строки: "Волшебники данных решили задачи за 18015.2 с !"

print("Волшебники данных решили задачи за {} с !".format(team1_time))

# Использование f-строк:
#     1. Переменные: количество решённых задач по командам: score_1, score_2
#     2. Пример итоговой строки: "Команды решили 40 и 42 задач.”

print(f"Команды решили {score_1} и {score_2} задач.")

#     1. Переменные: исход соревнования (challenge_result).
#     2. Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"

print(f"Результат битвы: {challenge_result}")

#     1. Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
#     2. Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")


#
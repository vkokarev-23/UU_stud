# Задача "Рассылка писем"
#
# Часто при разработке и работе с рассылками писем (e-mail) они отправляются от одного и того же
# пользователя (администрации или службы поддержки). Тем не менее должна быть возможность
# сменить его в редких случаях.
#
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
#
# Внутри функции реализовать следующую логику:
#
#     1. Проверка на корректность e-mail отправителя и получателя.
#     2. Проверка на отправку самому себе.
#     3. Проверка на отправителя по умолчанию.
#
# Пункты задачи:
#
#     1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient (получатель)
#        и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
#     2. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести
#        на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#     3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
#     4. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
#        "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
#     5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
#        Письмо отправлено с адреса <sender> на адрес <recipient>."
#     6. Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#     7. За один вызов функции выводится только одно из перечисленных уведомлений!
#        Проверки перечислены по мере выполнения.


def good_email(p_addr):
    e_addr = str(p_addr)

    if not '@' in e_addr:
        return False

    pattern_list = ['com', 'net', 'ru']
    for pattern in pattern_list:
        if pattern == e_addr.split('.')[-1]:    # режем строку по точкам, смотрим последний элемент
            # print(f"{pattern = }")            # нельзя "in" - пропускает: rus, comm и т.д.
            return True
    return False


def print_msg(msg, snd, rcp):
    print(msg)
    print(f"sender =     {snd}")
    print(f"recipient =  {rcp}")


def send_email(message, recipient, sender = 'university.help@gmail.com'):
    print()

    if not good_email(recipient, ) or not good_email(sender):
        print_msg('Невозможно отправить письмо с адреса <sender> на адрес <recipient>', sender, recipient)
        return

    if recipient == sender:
        print_msg('Нельзя отправить письмо самому себе!', sender, recipient)
        return

    # std_sender = 'university.help@gmail.com'
    std_sender = send_email.__defaults__[0]
    if  sender != std_sender:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!')
    print_msg('Письмо успешно отправлено с адреса <sender> на адрес <recipient>', sender, recipient)


# =================================
# Тесты:
a1 = 'university.help@gmail.com'
b1 = 'university.help@gmail.rus'

a2 = 'student_43.help@gmail.com'
b2 = 'student_43.help@gmail.comm'

ms = 'Бобры загрызли Буратино!'

send_email(ms, b1, sender=b2)
send_email(ms, a1, sender=b2)
send_email(ms, b1, sender=a2)

send_email(ms, a1, a1)
send_email(ms, a1, a2)
send_email(ms, a2)

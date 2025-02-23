def bubble_sort(ls):
    # чтобы цикл сработал хотя бы один раз, задаем значение переменной True
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swap = True


def selection_sort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        low = i
        # цикл для перебора неотсортированных элементов
        for j in range(i+1, len(ls)):
            if ls[j] < ls[low]:
                low = j
        # самый минимальный элемент меняем с первым элементом
        ls[i],  ls[low] = ls[low], ls[i]


def insertion_sort(ls):
    # Начинаем сортировать со второго элемента, так как первый элемент считается отсортированным
    for i in range(1, len(ls)):
        item = ls[i]
        # берем элемент для вставки и сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # отсортированный кусок списка двигаем вперед, если он больше элемента для вставки
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        # вставляем элемент
        ls[j + 1] = item


# ==========================================================================
# добавим счетчик итераций

def bubble_sort_1(ls):
    # чтобы цикл сработал хотя бы один раз, задаем значение переменной True

    iter_count = 0
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            iter_count += 1
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swap = True
    return iter_count


def bubble_sort_2(ls):
    """
    implements the classic bubble sort method
    :param ls: list of integers to be sorted
    :return: number of iterations
    """
    iter_count = 0
    first_verifiable = 0
    last_verifiable = len(ls) - 1
    while True:
        swaped = False
        for i in range(first_verifiable, last_verifiable):
            iter_count += 1
            if ls[i] > ls[i + 1]:
                if not swaped:
                    first_verifiable = 0 if i == 0 else i - 1
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swaped = True
        if not swaped:
            return iter_count


def selection_sort_1(ls):
    # i - количество отсортированных элементов
    iter_count = 0
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        low = i
        # цикл для перебора неотсортированных элементов
        for j in range(i+1, len(ls)):
            iter_count += 1
            if ls[j] < ls[low]:
                low = j
        # самый минимальный элемент меняем с первым элементом
        ls[i],  ls[low] = ls[low], ls[i]
    return iter_count


def insertion_sort_1(ls):
    # Начинаем сортировать со второго элемента, так как первый элемент считается отсортированным
    iter_count = 0
    for i in range(1, len(ls)):
        item = ls[i]
        # берем элемент для вставки и сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # отсортированный кусок списка двигаем вперед, если он больше элемента для вставки
        while j >= 0 and ls[j] > item:
            iter_count += 1
            ls[j + 1] = ls[j]
            j -= 1
        # вставляем элемент
        ls[j + 1] = item
    return iter_count



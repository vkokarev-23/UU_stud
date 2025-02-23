from math import inf


def divide(first, second):
    '''
    выполняет деление first/second, возвращает частное,
    а при делении на ноль - inf (infinity - бесконечность)
    '''
    return first / second if second != 0 else inf

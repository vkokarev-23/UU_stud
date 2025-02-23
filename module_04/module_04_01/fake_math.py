def divide(first, second):
    """
    выполняет деление first/second, возвращает частное,
    а при делении на ноль - строку "Ошибка"
    """
    return first / second if second != 0 else 'Ошибка'

def multiply_elements(factor, elements):
    """
    Пример функции для проверки стиля (PEP8).
    После запуска 'make format' здесь поправятся отступы и пробелы.
    """
    result = [item * factor for item in elements]
    return result


if __name__ == "__main__":
    items = [1, 2, 3]
    print(multiply_elements(10, items))
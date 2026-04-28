def add(a: int, b: int) -> int:
    """Складывает два целых числа с проверкой типов."""
    return a + b

if __name__ == "__main__":
    # Правильный вызов (int, int)
    val1 = 10
    val2 = 20
    result = add(val1, val2)
    print(f"Calculation: {val1} + {val2} = {result}")
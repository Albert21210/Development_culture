// Описание

# Simple Math Calculator: Элегантные вычисления в Python

## Введение
Цель проекта — продемонстрировать использование паттерна "Fluent Interface" для создания читаемого математического кода. Библиотека позволяет строить цепочки операций, минимизируя количество промежуточных переменных.

## Логика работы
Сердцем библиотеки является класс `Calculator`, методы которого возвращают `self`, позволяя вызывать их последовательно.

### Пример использования:
```python
from math_flow import Calculator

res = Calculator(10).add(5).multiply(2).result()
print(res) # 30

// Установка

pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) simple-math-flow

// Ссылка на репозиторий

https://github.com/Albert21210/Development_culture


---

// Исходный код (`src/math_flow/`)

#### `__init__.py`
Для красивого импорта.

```python
from .calculator import Calculator

__all__ = ["Calculator"]
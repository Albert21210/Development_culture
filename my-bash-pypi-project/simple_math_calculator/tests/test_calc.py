import pytest
from math_flow.calculator import Calculator

def test_basic_ops():
    calc = Calculator(10).add(5).subtract(3)
    assert calc.result() == 12

def test_multiplication():
    assert Calculator(2).multiply(5).result() == 10

def test_division_by_zero():
    with pytest.raises(ValueError):
        Calculator(10).divide(0)
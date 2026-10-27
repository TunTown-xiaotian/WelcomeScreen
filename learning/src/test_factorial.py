import pytest
from factorial import factorial


def test_factorial_positive_integer():
    assert factorial(3)==6
    assert factorial(5)==120
def test_factorial_boundary():
    assert factorial(0)==1
    assert factorial(1)==1
def test_factorial_positive_number():
    with pytest.raises(ValueError):
        factorial(-2)
def test_factorial_non_integer():
    with pytest.raises(TypeError):
        factorial(3.5)


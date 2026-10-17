import pytest
from math_operations import add, divide
from data_validator import is_valid_number

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    # Memastikan error muncul jika dibagi 0
    with pytest.raises(ValueError):
        divide(10, 0)

def test_is_valid_number():
    assert is_valid_number("10") == True
    assert is_valid_number("10.5") == True
    assert is_valid_number("abc") == False
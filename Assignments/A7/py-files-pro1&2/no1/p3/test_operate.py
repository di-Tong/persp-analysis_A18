#test_operate.py
import pytest
import operate

def test_operate():
    assert operate.operate(1, 2, '+') == 3, "incorrect result"
    assert operate.operate(3, 2, '-') == 1, "incorrect result"
    assert operate.operate(3, 2, '*') == 6, "incorrect result"
    assert operate.operate(4, 2, '/') == 2, "incorrect result"
    with pytest.raises(ZeroDivisionError) as excinfo:
        operate.operate(4, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(TypeError) as excinfo:
        operate.operate(4, 0, 3)
    assert excinfo.value.args[0] == "oper must be a string"
    with pytest.raises(ValueError) as excinfo:
        operate.operate(4, 0, '%')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"  
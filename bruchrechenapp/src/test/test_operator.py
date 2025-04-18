import pytest
from bruchrechenapp.src.model.operator import Operator
from bruchrechenapp.src.model.bruch import Bruch

def test_operator_plus():
    operand1 = Bruch(1, 2)
    operand2 = Bruch(1, 3)
    result = Operator.PLUS.berechne(operand1, operand2)
    assert result == Bruch(5, 6)

def test_operator_minus():
    operand1 = Bruch(1, 2)
    operand2 = Bruch(1, 3)
    result = Operator.MINUS.berechne(operand1, operand2)
    assert result == Bruch(1, 6)

def test_operator_mult():
    operand1 = Bruch(1, 2)
    operand2 = Bruch(1, 3)
    result = Operator.MULT.berechne(operand1, operand2)
    assert result == Bruch(1, 6)

def test_operator_div():
    operand1 = Bruch(1, 2)
    operand2 = Bruch(1, 3)
    result = Operator.DIV.berechne(operand1, operand2)
    assert result == Bruch(3, 2)

def test_operator_div_by_zero():
    operand1 = Bruch(1, 2)
    operand2 = Bruch(0, 1)
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operator.DIV.berechne(operand1, operand2)

def test_operator_string():
    assert Bruch(5,6) == Operator('+').berechne(Bruch(1,2), Bruch(1,3))
    assert Bruch(1,6) == Operator('-').berechne(Bruch(1,2),  Bruch(1,3))
    assert Bruch(1,2) == Operator('*').berechne(Bruch(3,4),  Bruch(2,3))
    assert Bruch(1,2) == Operator('/').berechne(Bruch(3,4),  Bruch(3,2))
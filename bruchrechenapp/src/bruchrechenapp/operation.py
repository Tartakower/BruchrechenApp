from enum import Enum

from bruchrechenapp.bruch import Bruch

class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = ":"

    def berechne(self, operand1: Bruch, operand2: Bruch) -> Bruch:
        if self == Operator.PLUS:
            return operand1.addiere(operand2)
        elif self == Operator.MINUS:
            return operand1.subtrahiere(operand2)
        elif self == Operator.MULT:
            return operand1.multipliziere(operand2)
        elif self == Operator.DIV:
            if operand2.zaehler == 0:
                raise ValueError("Division by zero is not allowed.")
            return operand1.dividiere(operand2)
        else:
            raise ValueError("Invalid operator.")
        
    def __str__(self) -> str:
        return self.value
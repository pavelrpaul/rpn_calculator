import pytest
from calculators import RPNCalculator

class TestCalclator:
    rpn_calc = RPNCalculator()
    good_string = "2 2 +"
    good_string_ans = 4
    bad_string = "w 2 2 +"
    bad_string_ans = None
    syntax_error_string = "2 2 + +"
    syntax_error_string_ans = 'Syntax error with operators'

    def test_add(self):
        x , y = 2, 3
        assert x + y == self.rpn_calc.add(x, y)

    def test_sub(self):
        x , y = 5, 3
        assert x - y == self.rpn_calc.sub(x, y)

    def test_mul(self):
        x , y = 2, 3
        assert x * y == self.rpn_calc.mul(x, y)

    def test_div(self):
        x , y = 6, 3
        assert x / y == self.rpn_calc.div(x, y)

    def test_good_string(self):
        assert self.good_string_ans == self.rpn_calc.calc(self.good_string)

    def test_bad_string(self):
        assert self.bad_string_ans == self.rpn_calc.calc(self.bad_string)

    def test_syntax_error_string(self):
        assert self.syntax_error_string_ans == self.rpn_calc.calc(self.syntax_error_string)

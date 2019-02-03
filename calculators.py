import re

from exceptions import TokenError

class BaseCalculator:
    """
    Basic Calculator methods and operators
    """
    def __init__(self):
        self.operators = {
            '+': self.add,
            '-': self.sub, 
            '*': self.mul,
            '/': self.div,
        }
        operators_regex = r''.join("/{}".format(key) for key in self.operators.keys())
        self.validator_regex = r'^[\d {}]+$'.format(operators_regex)


    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        return x / y

    def cacl(self, calc_string):
        raise NotImplementedError



class RPNCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.stack = []

    def _validator(func):
        def wrapper(self, calc_string):
            if re.match(self.validator_regex, calc_string):
                return func(self, calc_string)
        return wrapper

    @_validator
    def calc(self, calc_string):
        for token in calc_string.split():
            if self.operators.get(token):
                try:
                    op2, op1 = self.stack.pop(), self.stack.pop()
                except Exception as e:
                    return 'Syntax error with operators'
                self.stack.append(self.operators[token](op1,op2))
            elif token:
                self.stack.append(float(token))
            else:
                return 'Unknown error'
        try:
            data = self.stack.pop()
            self.stack = []
            return data
        except Exception as e:
            return 'Empty stack error'
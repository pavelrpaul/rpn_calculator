import sys
from pathlib import Path

from calculators import RPNCalculator

def main():
    if len (sys.argv) != 2 :
        print ("Usage: python main.py file_name")
        return
    file_name = sys.argv[1]
    rpn_calculator = RPNCalculator()
    try:
        with open(file_name, 'r') as f:
            for line in f:
                print(rpn_calculator.calc(line))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

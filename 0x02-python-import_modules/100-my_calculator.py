#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import  add, sub, mul, div
    import sys
    arg = sys.argv
    n = len(arg) - 1
    if n == 3:
        op = arg[2]
        a = int(arg[1])
        b = int(arg[3])
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

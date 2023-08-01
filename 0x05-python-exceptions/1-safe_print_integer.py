#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format9(value))
        return True
    except:
        return False

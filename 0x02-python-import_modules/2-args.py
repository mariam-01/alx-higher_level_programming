#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    a = sys.argv

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("1: {}".format(a[1]))
    else:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, a[i]))

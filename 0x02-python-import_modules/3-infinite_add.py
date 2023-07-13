#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    a = sys.argv
    s = 0
    if n == 0:
        print("0")
    else:
        for i in range(1, n + 1):
            s += int(a[i])
        print("{}".format(s))

#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print("{:c}{:c}".format(i + 32, i), end='')

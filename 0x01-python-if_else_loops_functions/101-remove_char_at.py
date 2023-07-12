#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    if (n < len(str) and n >= 0):
        for c in str:
            if c != str[n]:
                copy += c
    else:
        return str
    return copy

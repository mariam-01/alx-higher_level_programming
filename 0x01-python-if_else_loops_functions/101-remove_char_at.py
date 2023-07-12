#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    for c in str:
        if c == str[n]:
            copy = copy
        else:
            copy += c
    return copy    


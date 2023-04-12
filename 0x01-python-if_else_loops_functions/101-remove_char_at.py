#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = list()
    for i in range(len(str)):
        if i == n:
            continue
        else:
            str_copy.append(str[i])
    return "".join(str_copy)

#!/usr/bin/python3
def uppercase(str):
    strd = list()
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            strd.append(chr(ord(i) - 32))
        else:
            strd.append(i)
    print('{}'.format("".join(strd)), end='')
    print()

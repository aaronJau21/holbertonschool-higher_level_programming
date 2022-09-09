#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if islower(i):
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print("")


def islower(c):
    if ord(c) < 97:
        return False
    elif ord(c) >= 97 and ord(c) <= 122:
        return True

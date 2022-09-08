#!/usr/bin/python3

for a in range(26):
    if a != 4 and a != 16:
        print("{:s}".format(chr(a + ord("a"))), end="")

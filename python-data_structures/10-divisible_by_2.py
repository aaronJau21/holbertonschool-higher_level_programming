#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for num in my_list:
        if (num % 2) == 0:
            res.append(True)
        else:
            res.append(False)
    return res

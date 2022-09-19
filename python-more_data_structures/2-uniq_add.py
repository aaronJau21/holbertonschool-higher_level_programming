#!/usr/bin/python3
def uniq_add(my_list=[]):
    no_copies = 0

    for num in set(my_list):
        no_copies += num

    return (no_copies)

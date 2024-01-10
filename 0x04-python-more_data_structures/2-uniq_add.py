#!/usr/bin/python3
def uniq_add(my_list=[]):
    list1 = set(my_list)
    res = 0
    for num in list1:
        res += num
    return res

#!/bin/python3

def move_zeros(lst):
    n = [x for x in lst if x == 0]
    p = [x for x in lst if x != 0]
    p.extend(n)
    return p


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

#!/usr/bin/python3

def get_length_of_missing_array(arrays):
    arrays = [len(a) if a is not None else 0 for a in arrays ]
    arrays.sort()
    if 0 in arrays or len(arrays) == 0 : return 0
    for i in range(len(arrays)):
        if arrays[i+1] != arrays[i] + 1: return arrays[i]+1

#!/usr/bin/python

def flatten(a):
    nums = []
    for i in a:
        if type(i) == list:
            nums += flatten(i)
        else:
            nums.append(i)
    return nums

a = [1, [2,3], [[[4]]], [3,4], [2, [6, [1,2,3, [5]]]]]

print(a)
print flatten(a)

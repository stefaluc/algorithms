#!/usr/bin/python
def isPresent(array, num):
    for i in array:
        if num == i:
            return True
    return False

def missing(a, b):
    for i in a:
        if not isPresent(b, i):
            print i

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 6, 7]

missing(a, b)

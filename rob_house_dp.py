#!/usr/bin/python

def maxRob(houses, i = 0, val = 0, mem = {}):
    print mem
    if i >= len(houses):
        return val
    key = str(i) + '-' + str(val)
    if key in mem:
        return mem[key]
    mem[key] = max(maxRob(houses, i+1, val), maxRob(houses, i+2, val+houses[i]))
    return mem[key]

print maxRob([5, 0, 4, 6, 10])
#print maxRob([6, 7, 1, 3, 8, 2, 4])
#print maxRob([5, 3, 4, 11, 2])

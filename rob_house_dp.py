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

def maxRobBottomUp(houses):
    dp = [0] * len(houses)

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])

    return dp[-1]

# print maxRob([5, 0, 4, 6, 10])
# print maxRob([6, 7, 1, 3, 8, 2, 4])
# print maxRob([5, 3, 4, 11, 2])
print maxRobBottomUp([5, 0, 4, 6, 10])

#!/usr/bin/python
def climbStairs(stairsLeft, mem = {}):
    if stairsLeft == 0:
        return 1
    elif stairsLeft < 0:
        return 0
    
    numWays = 0
    for i in range(1, 4):
        key = str(i) + ',' + str(stairsLeft - i)
        if key in mem:
            numWays += mem[key]
        else:
            mem[key] = climbStairs(stairsLeft - i, mem)
            numWays += mem[key]
    return numWays

print climbStairs(3)
print climbStairs(4)
print climbStairs(7)

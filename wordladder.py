#!/usr/bin/python
from collections import deque

def isAdjacent(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    return count == len(a) - 1

def shortestPath(wordDict, src, target):
    q = deque([(src, 1)])
    while len(q) > 0:
        curr, dis = q.popleft()
        if curr == target:
            return dis
        for i in wordDict:
            if isAdjacent(i, curr):
                q.append((i, dis + 1))
                wordDict.remove(i)
    return 0

wordDict = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
print shortestPath(wordDict, 'TOON', 'PLEA')

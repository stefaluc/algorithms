#!/usr/bin/python
from collections import deque

def flatten(a):
    q = deque()
    q.append(a)

    flattened = []
    while len(q) > 0:
        for i in q.popleft():
            if type(i) is int:
                flattened.append(i)
            else:
                q.append(i)
    return flattened


a = [1, [2,3], [[[4]]]]
print flatten(a)

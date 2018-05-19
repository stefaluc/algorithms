#!/usr/bin/python
def solution(S):
    x = 0
    maxsub = 0
    while x != len(S):
        # find starting
        while x is not len(S) and not S[x].isupper():
            x += 1
        # find last
        y = x
        while y is not len(S) and not S[y].isdigit():
            y += 1

        length = y - x
        if length > maxsub:
            maxsub = length
        x = y
    if maxsub is 0:
        return -1
    else:
        return maxsub

S = 'Aa8aaaArtd900d'
T = 'AaaaaArtd900d'
print(solution(T))

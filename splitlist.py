#!/usr/bin/python

import math
def solution(S, K):
    key = S.upper()
    key = key.replace("-", "")
    interval = len(key) - K
    keylist = list(key)
    i = interval
    while i > 0:
        print i
        keylist.insert(i, "-")
        i -= K
    print i
    return "".join(keylist)

string = 'S-S-qWEQc2'
print solution(string, 3)

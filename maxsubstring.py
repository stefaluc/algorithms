#!/usr/bin/python

def frequent(s, k, l, m):
    subs = {} # maps substrings to number of occurences
    maxSub = 1
    for i in range(0, len(s)):
        j = k
        while j <= l and (i + j) <= len(s):
            print('i: %d, j: %d' % (i, j))
            curr = s[i:i+j]
            print curr
            # find number of distinct chars
            distinct = {}
            for char in curr:
                if distinct.has_key(char):
                    distinct[char] += 1
                else:
                    distinct[char] = 1
            if len(distinct) > m:
                break
            # increment/init substring key
            if subs.has_key(curr):
                subs[curr] += 1
            else:
                subs[curr] = 1
            print subs

            if subs[curr] > maxSub:
                maxSub = subs[curr]
            j += 1

    return maxSub

print frequent('abcabcabc', 1, 2, 26)


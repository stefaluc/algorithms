#!/usr/bin/python
def isMatching(a):
    pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for i in a:
        if pairs.has_key(i):
            stack.append(pairs[i])
        else:
            if len(stack) == 0:
                return False
            elif stack.pop() != i:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

a = '(({[]}))'
b = '(({))'
c = '(({]))'
d = ']['
e = '()()('
f = '{{[[(())]]}}'

print isMatching(a)
print isMatching(b)
print isMatching(c)
print isMatching(d)
print isMatching(e)
print isMatching(f)

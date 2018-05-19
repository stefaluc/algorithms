#!/usr/bin/python

def mergesort(a):
  if len(a) < 2:
    return a

  result = []
  mid = int(len(a)/2)
  x = mergesort(a[:mid])
  y = mergesort(a[mid:])

  while len(x) > 0 and len(y) > 0:
    if x[0] > y[0]:
      result.append(y[0])
      y.pop(0)
    else:
      result.append(x[0])
      x.pop(0)
  result += x
  result += y
  return result

array = [23, 41, 12, 61, 123, 11, 1, 22, 31, 21, 321, 1412, 12312, 123, 12,3, 23,1, 23,12,3,123, 13,1,4,2,4, 42,65,6,26, 3,62623,6,236,23,6,23,6,236,2,3,43,4,2,3,23,1,321,23,12,324,25,2,5,25,2,5,25,2,5,25,2,52,5,1,2,1,1,23,67,86,8,78,67,6,43,5623,45,8,789,7,97,9,79,79797,97,98]
print(mergesort(array))

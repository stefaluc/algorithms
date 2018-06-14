#!/usr/bin/python
def merge(array1, array2):
    ptr1 = 0
    ptr2 = 0
    merged = []
    while ptr1 <= len(array1):
        if ptr1 == len(array1):
            merged += array2[ptr2:]
            break
        elif ptr2 == len(array2):
            merged += array1[ptr1:]
            break
        elif array1[ptr1] < array2[ptr2]:
            merged.append(array1[ptr1])
            ptr1 += 1
        else:
            merged.append(array2[ptr2])
            ptr2 += 1
    return merged

print merge([1,2,3], [4,5,6])
print merge([1,2,3], [3,5,6])
print merge([5,7,9], [4,6,8])
print merge([100], [4,6,8, 1000])
print merge([], [4,6,8, 1000])

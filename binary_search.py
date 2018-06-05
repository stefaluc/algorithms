#!/usr/bin/python
def bs(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target > nums[mid]:
            lo = mid + 1
        elif target < nums[mid]:
            hi = mid - 1
        else:
            print 'found at ' + str(mid)
            return
    print 'not found'

bs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
bs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2)
bs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 20)

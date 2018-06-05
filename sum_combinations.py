#!/usr/bin/python
numCombinations = 0
def combinations(nums, target, part = []):
    global numCombinations
    if sum(part) == target:
        numCombinations += 1
    elif sum(part) > target:
        return

    for num in nums:
        combinations(nums, target, part + [num])

combinations([1,2,3], 5)
print numCombinations

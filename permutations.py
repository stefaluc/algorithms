#!/usr/bin/python
def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    perms = []
    for idx, num in enumerate(nums):
        for p in permutations(nums[:idx] + nums[idx+1:]):
            perms.append([num] + p)

    return perms

print permutations([1,2,3])

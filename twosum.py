#!/usr/bin/python
import sys

nums = map(int, sys.stdin.readline().split())
target = int(sys.stdin.readline())

nums.sort()
pairs = []
i = 0
j = len(nums) - 1
while len(nums) and i != j:
  if nums[i] + nums[j] == target:
    num1 = nums[i]
    num2 = nums[j]
    pairs.append([num1, num2])
    nums.remove(num1)
    nums.remove(num2)
    i = 0
    j = len(nums) - 1
    continue
  if target > (nums[i] + nums[j]):
    i += 1
  else:
    j -= 1

for pair in pairs:
  print str(pair[0]) + ' ' + str(pair[1])

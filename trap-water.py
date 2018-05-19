#!/usr/bin/python
def trap(height):
    stack = list()
    index = 0
    water = 0
    while index < len(height):
        print stack
        if len(stack) == 0 or height[index] <= height[stack[len(stack)-1]]:
            stack.append(index)
            index += 1
        else:
            bottom = stack.pop()
            if len(stack) != 0:
                vol = (min(height[stack[len(stack)-1]], height[index]) - height[bottom]) * (index - stack[len(stack)-1] - 1)
                print vol
                water += vol
    return water

print trap([0,1,0,2,1,0,1,3,2,1,2,1])

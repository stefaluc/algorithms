#!/usr/bin/python
def solution(A):
    count = 0
    visited = [[False for i in range(0, len(A[0]))] for j in range(0, len(A))]
    # do dfs for every unique country
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if visited[i][j] is False:
                dfs(i, j, A[i][j], visited, A)
                count += 1 # full country marked visited, increment count
    print(visited)
    return count

def isValid(i, j, visited, color, A):
    # check valid index
    if i >= 0 and j >= 0 and i < len(A) and j < len(A[0]):
        # check not visited and part of coutnry
        if visited[i][j] is False and color is A[i][j]:
            return True
    return False

def dfs(i, j, a, visited, A):
    visited[i][j] = True
    # down
    if isValid(i+1, j, visited, a, A):
        dfs(i+1, j, A[i+1][j], visited, A)
    # up
    if isValid(i-1, j, visited, a, A):
        dfs(i-1, j, A[i-1][j], visited, A)
    # right
    if isValid(i, j+1, visited, a, A):
        dfs(i, j+1, A[i][j+1], visited, A)
    # left
    if isValid(i, j-1, visited, a, A):
        dfs(i, j-1, A[i][j-1], visited, A)


a = [[1,1,1], [2,2,2], [3,3,3]]

print(solution(a))

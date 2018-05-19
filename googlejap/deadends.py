#!/usr/bin/python
maze = [] # changes on each test case
visited = []

def isDeadEnd(row, col, pos):
    global maze
    if pos == 'left':
        return maze[row+1][col] == '#' and maze[row][col-1] == '#' and maze[row-1][col] == '#'
    elif pos == 'right':
        return maze[row+1][col] == '#' and maze[row][col+1] == '#' and maze[row-1][col] == '#'
    elif pos == 'up':
        # print row, col, maze[row+1][col], maze[row][col+1], maze[row][col-1]
        return maze[row-1][col] == '#' and maze[row][col+1] == '#' and maze[row][col-1] == '#'
    elif pos == 'down':
        return maze[row][col-1] == '#' and maze[row][col+1] == '#' and maze[row+1][col] == '#'
    elif pos == 'starting':
        return maze[row+1][col] == '#' and maze[row][col+1] == '#' and maze[row][col-1] == '#' and maze[row-1][col] == 'S'
    return False

def isValid(row, col):
    if maze[row][col] != '#' and row < len(maze) and row >= 0 and col < len(maze[0]) and col >= 0:
        if not visited[row][col]:
            return True

def traverse(row, col, pos):
    global visited 
    visited[row][col] = True
    # if cannot move, dead end has been reached
    if isDeadEnd(row, col, pos):
        if pos == 'starting':
            return (1, 'starting')
        return 1
    deadEnds = 0
    # left
    if isValid(row, col-1):
        deadEnds += traverse(row, col-1, 'left')
    # right
    if isValid(row, col+1):
        deadEnds += traverse(row, col+1, 'right')
    # up
    if isValid(row-1, col):
        deadEnds += traverse(row-1, col, 'up')
    # down
    if isValid(row+1, col):
        deadEnds += traverse(row+1, col, 'down')

    return deadEnds

def countDeadEnds(maze, rows, cols):
    num = traverse(1, 1, 'starting') # starting position of each maze
    if not type(num) is int:
        return num[0]
    return num - 1

def main():
    global maze
    global visited 
    input = [line.rstrip('\n') for line in open('sampleinput.txt')]
    input = [inp for inp in input if inp != '']
    numCases = int(input[0])
    i = 1
    cases = 1
    while i < len(input):
        rows = int(input[i][0])
        cols = int(input[i][2])
        maze = input[i+1:i+rows+1]
        visited = [[False for p in range(0, cols)] for q in range(0, rows)]
        numDeadEnds = countDeadEnds(maze, rows, cols)
        #print visited
        print 'Case #' + str(cases) + ': ' + str(numDeadEnds)
        i += rows+1
        cases += 1

main()

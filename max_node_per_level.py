from collection import deque

def mostDifferentNums(root):
    q = deque([root])
    maxLevel = {}
    while len(q) > 0:
        uniqueNodesInLevel = set()
	toBeAdded = []
        while len(q) > 0:
            curr = q.popleft()
            if curr not in uniqueNodesInLevel:
                maxLevel[curr.val] = maxLevel.get(curr.val, 0) + 1
                uniqueNodesInLevel.add(curr.val)
            toBeAdded.append(curr)
        for i in toBeAdded:
            if i.left:
                q.append(i.left)
            if i.right:
                q.append(i.right)
    maxVal = -1
    maxNode = None
    for key, val in maxLevel:
        if val > maxVal:
            maxVal = val
            maxNode = key
    return maxNode

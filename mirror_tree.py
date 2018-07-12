#!/usr/bin/python
class TreeNode():
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

def bfs(node):
    if node == None:
        return
    print(node.data)
    queue = []
    queue.append(node.left)
    queue.append(node.right)
    for i in queue:
        if i == None:
            continue
        print(i.data)
        queue.append(i.left)
        queue.append(i.right)


def main():
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    g.right = TreeNode(8)
    g.right.right = TreeNode(9)
    f.right = TreeNode(10)
    d.left = TreeNode(11)
    d.left.left = TreeNode(12)
    d.left.left.left = TreeNode(12)
    
    bfs(root)
    print '======'
    bfs(mirror(root))
    print '======'
    print getDepth(root)
    print '======'
    print largestValue(root)
    print '======'
    print isBalanced(root)

def mirror(root):
    if root.left == None and root.right == None:
        return root
    if root.left != None and root.right != None:
        tmp = root.left
        root.left = mirror(root.right)
        root.right = mirror(tmp)
    return root

def getDepth(root, depth = 0):
    if root == None:
        return depth
    depth += 1
    depthLeft = getDepth(root.left, depth)
    depthRight = getDepth(root.right, depth)
    
    return max(depthLeft, depthRight)

def largestValue(root):
    if root.left is None and root.right is None:
        return root.data
    elif root.left is None:
        return max(root.data, largestValue(root.right))
    elif root.right is None:
        return max(root.data, largestValue(root.left))
    return max(largestValue(root.left), largestValue(root.right))

def isBalanced(node):
    if node is None:
        return True

    depthLeft = getDepth(node.left)
    depthRight = getDepth(node.right)

    return abs(depthLeft - depthRight) < 2 and isBalanced(node.left) and isBalanced(node.right)

main()

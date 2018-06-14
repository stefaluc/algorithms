#!/usr/bin/python
class TreeNode():
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

def main():
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    root.left = b
    root.right = c
    b.left = d
    b.right = e
    e.right = TreeNode(6)
    e.right.right = TreeNode(7)
    e.right.right.right = TreeNode(8)

    bfs(root)
    print '===='
    print isBalanced(root)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def preorder(node):
    if node == None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

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

def isBalanced(node, depth = 1):
    if node is None:
        return depth

    depthLeft = isBalanced(node.left, depth + 1)
    depthRight = isBalanced(node.right, depth + 1)
    print depthRight, depthLeft

    return abs(depthLeft - depthRight) < 2

main()

#!/usr/bin/python
class Node():
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = next

class SinglyLinkedList():
    def __init__(self, head):
        self.head = Node(None, head)

    def insert(self, elem):
        insertNode = self.insert_ptr(elem)
        next = insertNode.next
        insertNode.next = Node(elem, next)

    def insert_ptr(self, elem):
        curr = self.head.next
        prev = self.head
        while curr is not None:
            if elem <= curr.elem:
                return prev
            prev = curr
            curr = curr.next
        return prev

    def find(self, elem):
        curr = self.head.next
        while curr is not None:
            if elem == curr.elem:
                return curr
            curr = curr.next
        return curr

    def remove(self, elem):
        curr = self.head.next
        prev = self.head
        while curr is not None:
            if elem == curr.elem:
                if prev is None:
                    curr = None
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def printList(self):
        curr = self.head
        while curr is not None:
            print curr.elem,
            curr = curr.next
        print

sll = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))

sll.printList()
sll.insert(5)
sll.printList()
sll.insert(0)
sll.printList()
sll.insert(4)
sll.printList()
sll.insert(2)
sll.printList()
print 'remove'
sll.remove(2)
sll.printList()
sll.remove(2)
sll.printList()
sll.remove(0)
sll.printList()
sll.remove(5)
sll.printList()
sll.remove(6)
sll.printList()
print 'find'
print sll.find(4).elem
sll.insert(7)
sll.printList()
print sll.find(7).elem
print sll.find(1).elem
print sll.find(0)

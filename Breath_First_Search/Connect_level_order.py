"""
Given a binary tree connect all level seccessor order.


"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = 0
        self.left = 0 
        self.next = 0

    def print_tree(self):
        current = self
        while current:
            print(str(current.value) + " ", end='')

            current = current.next

def connect_level_order(root):

    queue = deque() 
    queue.append(root)
    previousNode = None

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            current = queue.popleft()

            if previousNode:
                previousNode.next = current

            previousNode = current

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            
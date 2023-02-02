"""
Connect each of the binary tree to its level order.

The last node should point to null.

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7

"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = 0
        self.right = 0 
        self.next = 0 
    # 2
    def print_level_order(self):
        nextLevelRoot = self # 4
        while nextLevelRoot:
            current = nextLevelRoot # 2
            nextLevelRoot = None
            while current:
                print(str(current.value) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left 
                    elif current.right:
                        nextLevelRoot = current.right 
                current = current.next 
            print()


def connect_level_order(root):

    queue = deque() 

    queue.append(root)

    while queue:
        levelSize = len(queue)
        previousRoot =  None

        for i in range(levelSize):
            current = queue.popleft()

            if previousRoot:
                previousRoot.next = current
            
            previousRoot = current
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)



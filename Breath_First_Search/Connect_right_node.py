"""
Given a binary tree connect the right most node.

"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left, self.right, self.next = 0, 0, 0 


def right_most(root):
    queue = deque() 

    queue.append(root)
    head_node = root
    prev_node = None

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            last_index = levelSize -1
            current = queue.popleft()

            if i == last_index:
                if prev_node:
                    prev_node.next = current
                prev_node = current
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        
        return head_node




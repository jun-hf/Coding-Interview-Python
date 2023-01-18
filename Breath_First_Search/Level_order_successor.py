"""
Given a binary tree, find the level order successor

"""
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 

def level_order_successor(root, key):

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            currentNode = queue.popleft() 

            if currentNode.value == key:
                return queue.popleft().value

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)
            




def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)

    print(level_order_successor(root, 3))

main()
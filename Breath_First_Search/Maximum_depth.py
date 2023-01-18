"""
Find the maximum depth of a binary tree.

"""

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

def maximum_depth(root):
    max_depth = 0 

    queue = deque() 
    queue.append(root)

    while queue:
        levelSize = len(queue)
        max_depth += 1

        for i in range(levelSize):
            currentNode = queue.popleft()

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)

    
    return max_depth

def main():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(9)

    root.left.left = TreeNode(8)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(8)

    root.left.left.left = TreeNode(8)

    print(maximum_depth(root))

main()

    

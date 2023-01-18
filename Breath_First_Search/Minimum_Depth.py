"""
Find the minimum depth of a binary tree.

        1
      /   \
      2    3
    /  \  
   4   5  

1 - 3 : 2 

I want search each level of the node while having a counter which level you are in and the moment

"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimum_depth(root):
    counter = 0
    queue = deque()
    queue.append(root)

    if root.left ==None or root.right == None:
        return 1

    while queue:
        counter += 1
        levelSize = len(queue)
        
        for i in range(levelSize):
            currentNode = queue.popleft()

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)
            
            if currentNode.left == None and currentNode.right == None:
                return counter

def main():

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.left.left = TreeNode(8)
    root.right = TreeNode(7)

    print(minimum_depth(root))

main()
"""
Given a binary tree, populate an array to represent its level-by-level traversal.

You should populate the values of all nodes of each level f4rom left to right in
seprate subarrays

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7

[[1], [2,3], [4,5,6,7]]

result = []

create a queue (deque())
[]

whiel queue:
    get the levelSize = len(queue)
    currentLevel = []

    for i in range(levelSize):
        currentNode = queue.popleft() 
        currentLevel.append(currentLevel.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    
    result.append(currentLevel)

return result


"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def traverse(root):
    result = []

    queue = deque()
    queue.append(root)
    """
    result = [[1], ]
    queue = [2,3]

    levelSize = 2
    currentLevel = []

    currentNode = root
    
    
    """

    while queue:
        levelSize = len(queue)
        currentLevel = []

        for i in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.value)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        result.append(currentLevel)
    
    return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)

    print(traverse(root))

main()
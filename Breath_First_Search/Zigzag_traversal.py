"""
Given a binary tree, populate an array to represent its zigzag level order through traversal.

Populate values from left to right then right to left.

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7

[[1], [3,2], [4,5,6,7]]

design:

result = [[1], ]

queue = [4,5]
left_to_right = false

while queue:
    levelSize = len(queue) : 2
    currentLevel = deque() [3,2]

    for i in range(levelSize): 0, 1
        currentNode = queue.popleft : 3
        
        if left_to_right:
            currentLevel.append(currentNode.value)
        else:
            currentLevel.appendlefft(currentNode.value)
        
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        
    
    left_to_right = !left_to_right
    result.append(currentLevel)

return result
"""
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def zigZag_traversal(root):

    result = []

    queue = deque()
    queue.append(root)
    left_to_right = True

    while queue:
        currentSize = len(queue)
        currentLevel = deque()

        for i in range(currentSize):
            currentNode = queue.popleft()

            if left_to_right:
                currentLevel.append(currentNode.value)
            else:
                currentLevel.appendleft(currentNode.value)
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        left_to_right = not left_to_right
        result.append(list(currentLevel))

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)

    print(zigZag_traversal(root))

main()
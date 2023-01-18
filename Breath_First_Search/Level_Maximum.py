"""
Find the maximum value from each level in a binary tree

        1
      /   \
      6    3
    /  \  / \
   3   9  6  9

result = [1, 6, 9]

"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

def level_maximum(root):

    result = [] 

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelMax = 0

        for i in range(levelSize):
            currentNode = queue.popleft()

            levelMax = max(levelMax, currentNode.value)

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(levelMax)

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(8)
    root.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(88)

    print(level_maximum(root))

main()
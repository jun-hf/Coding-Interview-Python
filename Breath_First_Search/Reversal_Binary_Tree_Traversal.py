"""
Given a binary tree, populate an array to represent its level-by-level
traversal in reversa order.

Populate the values of all ndoes in each level from left to right in
separate sub-arrays

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7

[[4,5,6,7], [2,3], [1]]


"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = 0, 0


def reverseTraversal(root):
    result = deque()

    queue = deque()
    queue.append(root)

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
        
        result.appendleft(currentLevel)
    
    return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)

    print(reverseTraversal(root))

main()

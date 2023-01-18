"""
Find the level avarages of a given binary tree.

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7
result = [1, 2.5]
queue = [ 4, 5, 6, 7]

design:

def level_avarage(root):
    result = [] 
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue) : 2
        levelSum = 0 : 5

        for i in range(levelSize): 0, 1
            currentNode = queue.popleft() : 3

            levelSum += currentNode.value

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        result.append(levelSum/levelSize)
    
    return result

"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_average(root):
    result = [] 

    queue = deque() 
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelSum = 0

        for i in range(levelSize):
            currentNode = queue.popleft()

            levelSum += currentNode.value

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(levelSum/levelSize)
    
    return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(level_average(root))
        


main()
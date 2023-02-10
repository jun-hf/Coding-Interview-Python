"""
Given a binary tree and a sum find any path that is equal to sum. 



"""

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

def count_paths(root, S):
    return count_paths_recur(root, S, [])

def count_paths_recur(currentNode, S, currentPath):

    if currentNode is None:
        return 0 

    currentPath.append(currentNode.val)
    pathCount = 0
    pathSum = 0 

    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]

        if pathSum == S:
            pathCount += 1 
    
    pathCount += count_paths_recur(currentNode.left, S, currentPath)

    pathCount += count_paths_recur(currentNode.right, S, currentPath )

    del currentPath[-1]

    return pathCount





for i in range(6, -1, -1):
    print(i)
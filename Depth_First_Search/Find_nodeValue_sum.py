"""
Given a binary tree where the node value can have only 0-9, find the total sum of all path

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7


124 + 125 + 136 + 137 = sum

Design:

# node = 
sum = 1


def find_root_summ(node, sum):
    if node is none:
        return 0

    sum = sum*10 + node.value

    if node.left is None and node.right is None:
        return sum

    return find_root_sum(node.left, sum) + find_root_sum(node.right, sum)


"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

def find_sum(root):
    return find_path_sum(root, 0)

def find_path_sum(root, sum):

    if root is None: 
        return 0 

    sum = sum*10 + root.value

    if root.left is None and root.right is None:
        return sum

    return find_path_sum(root.left, sum) + find_path_sum(root.right, sum)

    

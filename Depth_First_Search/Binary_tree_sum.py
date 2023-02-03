"""
Given a binary tree and a value X, find the if there
is a total sum from the root to leaf node == X.


Design:
Using recersive call. 

space: the call stack o(n)


def path_sum(node, x):

    if node == None:
        return False

    if node.value == x and (node.left is None and node.right is None):
        return True

    return path_sum(node.left, x-node.value) or path(node.right, v-node.value)

"""

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None

def path_sum(node, x):
    if node == None:
        return False

    if node.value == x and node.left == None and node.right == None:
        return True

    next_x = x - node.value

    return path_sum(node.left,next_x) or path_sum(node.right, next_x)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)

    print(path_sum(root, 8))

main()
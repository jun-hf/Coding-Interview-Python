"""
Given a binary tree and a sequence,
check if the sequence is within the bianry tree.


        1 t
      /   \
(false)8    5 t
    /  \  / \
   9   5  4f  7 t

[1, 5, 7]

root = 7

seq =[7]

def find_seq(root, seq):
    if root is None:
        return False

    if root.left and root.right is none and root.value == seq[0]

    if seq[0] == value:
    return find_seq(root.left, seq[1:]) or find_seq(root.right, seq[1:])

    

    return False
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None 
        self.left = None


def find_seq(root, seq):

    if root is None:
        return False

    if root.left is None and root.right is None and root.value == seq[0]:
        return True

    if root.value == seq[0]:
        return find_seq(root.left, seq[1:]) or find_seq(root.right, seq[1:])

    return False

def main():
    root = TreeNode(1)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.left = TreeNode(7)

    print(find_seq(root, [1, 5, 7]))

# main()

a = [2, 3, 4]

print(a)

b = a[1:]

print(b)

b[0] = 9

print(a, b)


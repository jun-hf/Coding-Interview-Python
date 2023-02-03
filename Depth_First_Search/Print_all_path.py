"""
Print all the path of a binary tree


Design:
"""

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None


def print_all_path(root, stack):

    if root is None:
        return 

    stack.append(root)
    if root.left is None and root.right is None:
        print(" ".join(str(i.value) for i in stack))

    print_all_path(root.left, stack)
    print_all_path(root.right, stack)
    stack.pop()





def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(print_all_path(root, []))

main()
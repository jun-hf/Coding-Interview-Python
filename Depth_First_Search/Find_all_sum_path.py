"""
Given a bianry tree find all path that has a path sum x.

        14
      /   \
      8    9
    /  \  / \
   4   2  1  7

x = 24

Design:

Traverse all path. 
keep a list if the there is path there is == X then add it to the list ? store the list

        14
      /   \
      8    9
    /  \  / \
   4   2  1  7

   root = 9
   x = 10
   s1 = [[14, 8,2 ]] 
   s2 = [14, 9] 
   root_node = 14
all_path(root, s1, s2, x, root_node):

    if root == None:
        return

    s2.append()
    if root.value == x and root.left == None and root.right == None:
        s1.append(s2)

    all_path(root.left, s1, s2,x - root.value, root_node)
    all_path(root.right, s1, s2, x- root.value, root_node) 

    s2.pop()

    if root == root_node:
        return s1
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def sum_all_path(node, result_stack, path_stack, target, root):

    if node == None:
        return

    path_stack.append(node.value)

    if node.value == target and node.left == None and node.right == None:
        stack = []
        for i in range(len(path_stack)):
            stack.append(path_stack[i])

        result_stack.append(stack)


    sum_all_path(node.left, result_stack, path_stack, target - node.value, root)
    sum_all_path(node.right, result_stack, path_stack, target - node.value, root)

    path_stack.pop()

    if node == root:
        return result_stack


def main():
    root = TreeNode(14)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)

    print(sum_all_path(root, [], [], 24, root))

main()
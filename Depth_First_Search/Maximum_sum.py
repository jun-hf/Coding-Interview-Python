"""
Find the max sum of the binary tree

        1
      /   \
      2    3
    /  \  / \
   4   5  6  7

"""

class TreeNode:
    def __init__(self, value):
        self.value = value


class TreeSum:

    def __init__(self):
        self.max = 0

    def find_max_sum(self, root):
        self.find_local_sum(root)

        return self.max

    def find_local_sum(self, node):
        if node == None:
            return 0

        left_sum = self.find_local_sum(node.left)
        right_sum = self.find_local_sum(node.right)

        current_sum = left_sum + right_sum + node.value

        self.max = max(current_sum, self.max)

        return max(left_sum, right_sum) + node.value
"""
Given a binary tree find the longest distance between 2 leaf node.

The path dont have to pass through root.

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeLongestPath:
    def __init__(self):
        self.longest_path = 0


    def calculate_longest_path(self, root):
        pass

    def find_height(self, node):
        if node == None:
            return 0

        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)

        current_path = left_height + right_height + 1

        self.longest_path = max(self.longest_path, current_path)

        return max(left_height, right_height) + 1
    
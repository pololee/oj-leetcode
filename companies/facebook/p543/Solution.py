class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution:
    def diameter_of_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        if not root or (root.left is None and root.right is None):
            return 0

        self.diameter = 0

        self.max_depth(root)
        return self.diameter
    
    def max_depth(self, root):
        if not root: return 0

        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)

        self.diameter = max(self.diameter, left_max_depth + right_max_depth)
        return max(left_max_depth, right_max_depth) + 1

class OptimizedSolution:
    def diameter_of_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        if not root or (root.left is None and root.right is None):
            return 0

        self.max_depths = dict()
        self.diameter = 0

        self.max_depth(root)
        return self.diameter

    def max_depth(self, root):
        if not root: return 0
        if root in self.max_depths: return self.max_depths[root]

        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)

        self.diameter = max(self.diameter, left_max_depth + right_max_depth)
        self.max_depths[root] = max(left_max_depth, right_max_depth) + 1
        return self.max_depths[root]

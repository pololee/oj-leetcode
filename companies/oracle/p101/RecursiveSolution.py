# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.is_symmetric_help(root.left, root.right)

    def is_symmetric_help(self, left, right):
        if not left or not right:
            return left == right

        if left.val != right.val:
            return False

        return self.is_symmetric_help(left.left, right.right) and self.is_symmetric_help(left.right, right.left)

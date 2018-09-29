# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        leftRt = self.lowestCommonAncestor(root.left, p, q)
        rightRt = self.lowestCommonAncestor(root.right, p, q)

        if leftRt and rightRt:
            return root

        if leftRt:
            return leftRt

        if rightRt:
            return rightRt

        return None

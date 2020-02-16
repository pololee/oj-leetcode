"""
Definition of TreeNode:
"""
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        if not root:
            return True

        stack = []
        prev = None
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            if not stack:
                break

            curr = stack.pop()
            if prev and prev.val >= curr.val:
                return False

            prev = curr
            curr = curr.right

        return True

class RecursiveSolution:
    def isValidBST(self, root):
        if not root:
            return True
    
    def dfs(self, root, minValue, maxValue):
        if not root:
            return True
        
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        return self.dfs(root.left, minValue, root.val) and self.dfs(root.right, root.val, maxValue)

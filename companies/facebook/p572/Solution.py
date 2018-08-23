class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype
        """
        if not s:
            return False
        if self.is_same(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s, t):
        if not s or not t:
            return s == t
        
        if s.val != t.val:
            return False
        
        return self.is_same(s.left, t.left) or self.is_same(s.right, t.right)

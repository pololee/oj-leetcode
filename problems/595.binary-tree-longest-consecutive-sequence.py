class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        self.longest = 0
        self.dfs(root, 1)

        return self.longest

    def dfs(self, root, curtLen):
        if not root:
            return

        self.longest = max(self.longest, curtLen)

        if root.left:
            if root.left.val == root.val + 1:
                self.dfs(root.left, curtLen + 1)
            else:
                self.dfs(root.left, 1)

        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right, curtLen + 1)
            else:
                self.dfs(root.right, 1)

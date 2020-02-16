# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []
        self.dfs_util(root, [], sum, results)
        return results

    def dfs_util(self, root, path, sum, results):
        if not root:
            return

        if not root.left and not root.right and sum - root.val == 0:
            path.append(root.val)
            results.append(list(path))
            path.pop()
            return

        if root.left:
            path.append(root.val)
            self.dfs_util(root.left, path, sum - root.val, results)
            path.pop()

        if root.right:
            path.append(root.val)
            self.dfs_util(root.right, path, sum - root.val, results)
            path.pop()

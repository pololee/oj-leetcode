# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        results = []
        self.height_util(root, results)
        return results

    def height_util(self, root, results):
        if not root:
            return -1

        height = 1 + max(self.height_util(root.left, results),
                         self.height_util(root.right, results))
        if height == len(results):
            results.append(list())
        results[height].append(root)

        return height

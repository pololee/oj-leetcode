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

        left = root.left
        right = root.right

        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False

        queue1 = collections.deque()
        queue1.append(left)
        queue2 = collections.deque()
        queue2.append(right)

        while queue1 and queue2:
            left = queue1.popleft()
            right = queue2.popleft()

            if not left and not right:
                continue

            if (not left and right) or (left and not right):
                return False

            if left.val != right.val:
                return False

            queue1.append(left.right)
            queue1.append(left.left)
            queue2.append(right.left)
            queue2.append(right.right)

        return True

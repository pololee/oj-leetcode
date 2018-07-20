# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.longest_consecutive_util(root, None, 0)

    def longest_consecutive_util(self, current, parent, length):
        if not current:
            return length

        if parent and parent.val + 1 == current.val:
            length += 1
        else:
            length = 1

        return max(
            length,
            max(
                self.longest_consecutive_util(current.left, current, length),
                self.longest_consecutive_util(current.right, current, length)
            )
        )


def main():
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    print(sol.longestConsecutive(root))


if __name__ == '__main__':
    main()

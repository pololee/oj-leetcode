# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        result += self.contain_path(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)

        return result

    def contain_path(self, root, sum):
        if not root:
            return 0

        result = 0
        if root.val == sum:
            result += 1

        result += self.(root.left, sum - root.val)
        result += self.(root.right, sum - root.val)

        return result


def main():
    sol = Solution()


if __name__ == '__main__':
    main()

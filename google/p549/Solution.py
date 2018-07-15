# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    class LongestUntilRoot:
        def __init__(self, increase, decrease):
            self.increase_to_root = increase
            # given a root, the longest increase consecutive sequence including the root
            # including the root, i.e. if no consecutive, it'll be just one
            self.decrease_to_root = decrease
            # given a root, the longest increase consecutive sequence including the root
            # including the root, i.e. if no consecutive, it'll be just one

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.max_length = 0
        self.longest_consecutive_dfs(root)

        return self.max_length

    def longest_consecutive_dfs(self, root):
        if not root:
            return self.LongestUntilRoot(0, 0)

        increase = 1  # at least it's one if no consecutive
        decrease = 1  # at least it's one if no consecutive
        if root.left:
            longest_until_left = self.longest_consecutive_dfs(root.left)
            if root.left.val + 1 == root.val:
                increase = max(
                    increase, longest_until_left.increase_to_root + 1)
            elif root.left.val - 1 == root.val:
                decrease = max(
                    decrease, longest_until_left.decrease_to_root + 1)

        if root.right:
            longest_until_right = self.longest_consecutive_dfs(root.right)
            if root.right.val + 1 == root.val:
                increase = max(
                    increase, longest_until_right.increase_to_root + 1)
            elif root.right.val - 1 == root.val:
                decrease = max(
                    decrease, longest_until_right.decrease_to_root + 1)

        self.max_length = max(self.max_length, increase + decrease - 1)
        return self.LongestUntilRoot(increase, decrease)

def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.longestConsecutive(root))

if __name__ == '__main__':
    main()

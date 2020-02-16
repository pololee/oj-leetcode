class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BetterSolution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype int
        """
        if not root:
            return 0

        self.path_sums_helper(root, sum)
        return self.count

    def path_sums_helper(self, root, sum):
        path_sums = []

        if not root:
            return path_sums

        left_path_sums = self.path_sums_helper(root.left, sum)
        right_path_sums = self.path_sums_helper(root.right, sum)

        path_sums.append(root.val)
        if root.val == sum:
            self.count += 1

        for k in left_path_sums:
            tmp = k + root.val
            if tmp == sum:
                self.count += 1
            path_sums.append(tmp)

        for k in right_path_sums:
            tmp = k + root.val
            if tmp == sum:
                self.count += 1
            path_sums.append(tmp)

        return path_sums

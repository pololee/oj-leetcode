from Solution import TreeNode

class DFSSolution:
    def average_of_levels(self, root):
        if not root:
            return []
        
        level_sum = []
        level_count = []
        self.average(root, 0, level_sum, level_count)

        results = []
        for i in range(len(level_sum)):
            results.append(level_sum[i] / level_count[i])
        return results
    
    def average(self, node, level, level_sum, level_count):
        """
        :node TreeNode
        :level: a number represent the current level
        :level_sum: an array, each element represent the sum of each level
        :level_count: an array, each element represent the number of node on each level
        """
        if not node:
            return
        
        if level < len(level_sum):
            level_sum[level] += node.val
            level_count[level] += 1
        else:
            level_sum.append(1.0 * node.val)
            level_count.append(1)
        
        self.average(node.left, level + 1, level_sum, level_count)
        self.average(node.right, level + 1, level_sum, level_count)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = DFSSolution()
    print(sol.average_of_levels(root))
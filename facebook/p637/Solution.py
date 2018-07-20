from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def average_of_levels(self, root):
        """
        :type root: TreeNode
        :rtype List[float]
        """
        if not root:
            return []
        
        results = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            val_sum = 0
            for _ in range(size):
                node = queue.popleft()
                val_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(val_sum / size)
        return results

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.average_of_levels(root))

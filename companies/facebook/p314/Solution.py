from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def vertical_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        if not root: return answer

        col_map = defaultdict(list)
        queue = deque()
        queue.append((0, root))

        min_col = 0
        max_col = 0

        while queue:
            col_index, node = queue.popleft()
            col_map[col_index].append(node.val)

            if node.left:
                queue.append((col_index-1, node.left))
                min_col = min(min_col, col_index - 1)
            if node.right:
                queue.append((col_index+1, node.right))
                max_col = min(max_col, col_index + 1)
        
        for col_index in range(min_col, max_col + 1):
            answer.append(col_map[col_index])
        
        return answer


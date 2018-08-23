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

        while queue:
            col_index, node = queue.popleft()
            col_map[col_index].append(node.val)

            if node.left:
                queue.append((col_index-1, node.left))
            if node.right:
                queue.append((col_index+1, node.right))
        
        for col_index in sorted(col_map):
            answer.append(col_map[col_index])
        
        return answer


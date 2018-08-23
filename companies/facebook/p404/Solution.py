import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sum_of_left_leaves(self, root):
        """
        :root type: TreeNode
        :rtype int
        """
        if not root:
            return 0
        
        answer = 0
        if root.left:
            if not root.left.left and not root.left.right:
                answer += root.left.val
            else:
                answer += self.sum_of_left_leaves(root.left)
        answer += self.sum_of_left_leaves(root.right)
        
        return answer
    
    def sum_of_left_leaves_bfs(self, root):
        if not root:
            return 0
        
        answer = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.pop()

            if node.left:
                if not node.left.left and not node.left.right:
                    answer += node.left.val
                else:
                    queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        return answer
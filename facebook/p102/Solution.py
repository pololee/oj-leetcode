import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root):
        """
        :root type: TreeNode
        :rtype list[list[int]]
        """
        if not root:
            return []

        answers = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            num_of_node_in_curr_level = len(queue)
            curr_level = []
            for _ in range(num_of_node_in_curr_level):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answers.append(curr_level)
        return answers

class AnotherSolution:
    def level_order(self, root):
    
    def recursive_bfs(self, root, level, answer):
        if not root:
            return

        if level >= len(answer):
            answer.append(list())
        
        answer[level].append(root.val)
        self.recursive_bfs(root.left, level + 1, answer)
        self.recursive_bfs(root.right, level + 1, answer)

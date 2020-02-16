# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque()
        queue.append(root)

        tmp = []
        while queue:
            node = queue.popleft()
            tmp.append(node)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        ans = []
        for node in tmp:
            if node:
                ans.append(str(node.val))
            else:
                ans.append("#")

        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        chars = data.split(',')
        size = len(chars)

        root = TreeNode(int(chars[0]))
        queue = deque()
        queue.append(root)

        i = 0
        while i + 2 < size:
            node = queue.popleft()

            i += 1
            if chars[i] != "#":
                left = TreeNode(int(chars[i]))
                node.left = left
                queue.append(left)

            i += 1
            if chars[i] != "#":
                right = TreeNode(int(chars[i]))
                node.right = right
                queue.append(right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

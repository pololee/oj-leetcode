# ### [449\. Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)

# Difficulty: **Medium**


# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# **The encoded string should be as compact as possible.**

# **Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# #### Solution

# Language: **Python**
# Definition for a binary tree node.

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        ans = []
        self.inorderDFS(root, ans)
        return ",".join([str(x) for x in ans])

    def inorderDFS(self, root, ans):
        if not root:
            return

        ans.append(root.val)
        self.inorderDFS(root.left, ans)
        self.inorderDFS(root.right, ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = [int(x) for x in data.split(',')]
        queue = collections.deque(data)

        return self.buildTree(queue)

    def buildTree(self, queue):
        if not queue:
            return None

        value = queue.popleft()
        root = TreeNode(value)

        small = collections.deque()
        while queue and queue[0] < value:
            small.append(queue.popleft())

        root.left = self.buildTree(small)
        root.right = self.buildTree(queue)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

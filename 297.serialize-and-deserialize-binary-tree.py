# ### [297\. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

# Difficulty: **Hard**


# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# **Example: **

# ```
# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# ```

# **Clarification:** The above format is the same as . You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# **Note: **Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# #### Solution

# Language: **Python**

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:
    SPLITER = ','
    NULL = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        ans = []
        self.preorderDFS(root, ans)
        return self.SPLITER.join(ans)

    def preorderDFS(self, root, ans):
        if not root:
            ans.append(self.NULL)
        else:
            ans.append(str(root.val))
            self.preorderDFS(root.left, ans)
            self.preorderDFS(root.right, ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        queue = collections.deque(data.split(self.SPLITER))
        return self.buildTree(queue)

    def buildTree(self, queue):
        if not queue:
            return

        value = queue.popleft()
        if value == self.NULL:
            return None

        root = TreeNode(int(value))
        root.left = self.buildTree(queue)
        root.right = self.buildTree(queue)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

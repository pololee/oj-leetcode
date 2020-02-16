# ### [285\. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)

# Difficulty: **Medium**


# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# The successor of a node `p` is the node with the smallest key greater than `p.val`.

# **Example 1:**

# ![](https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG)

# ```
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2\. Note that both p and the return value is of TreeNode type.
# ```

# **Example 2:**

# ![](https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG)

# ```
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
# ```

# **Note:**

# 1.  If the given node has no in-order successor in the tree, return `null`.
# 2.  It's guaranteed that the values of the tree are unique.


# #### Solution

# # Language: **Python3**

# # ```python3
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root

    def inorderPredecessor(self, root, p):
        if not root:
            return None

        if root.val >= p.val:
            return self.inorderPredecessor(root.left, p)
        else:
            right = self.inorderPredecessor(root.right, p)
            return right if right else root

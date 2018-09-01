# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            right_min_node = self.find(root.right)
            root.val = right_min_node.val
            root.right = self.deleteNode(root.right, right_min_node.val)
        
        return root
    
    def findMin(self, node):
        while node.left is not None:
            node = node.left
        
        return node

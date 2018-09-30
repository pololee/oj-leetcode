"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # write your code here
        dummy = TreeNode(0)
        dummy.left = root

        parent, node = self.findNode(dummy, root, value)
        if not node:
            return root

        self.deleteNode(parent, node)
        return dummy.left

    def findNode(self, parent, root, value):
        if not root:
            return [parent, None]

        if root.val == value:
            return [parent, root]
        elif root.val < value:
            return self.findNode(root, root.right, value)
        else:
            return self.findNode(root, root.left, value)

    def deleteNode(self, parent, node):
        if not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return

        father = node.right
        leftMost = father.left
        if leftMost is None:
            if parent.left == node:
                parent.left = father
            else:
                parent.right = father
            return

        while leftMost and leftMost.left:
            father = leftMost
            leftMost = leftMost.left

        father.left = leftMost.right
        if parent.left == node:
            parent.left = leftMost
        else:
            parent.right = leftMost

        leftMost.left = node.left
        leftMost.right = node.right
        node.left = None
        node.right = None


def main():
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    sol.removeNode(root, 5)

if __name__ == '__main__':
    main()

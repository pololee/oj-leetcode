# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        prevSlow = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        rootNode = slow
        afterRoot = slow.next
        prevSlow.next = None # cut the
        root = TreeNode(rootNode.val)
        if rootNode != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(afterRoot)
        return root



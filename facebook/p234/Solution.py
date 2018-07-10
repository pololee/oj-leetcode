# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # odd # of node in the list
        if fast:
            slow = slow.next
        # now slow is the start of the right half
        right_head = self.reverse(slow)
        left_head = head
        while left_head and right_head:
            if left_head.val != right_head.val:
                return False
            left_head = left_head.next
            right_head = right_head.next
        
        return True
    
    def reverse(self, head):
        if not head:
            return head
        
        return self.reverse_util(None, head)

    def reverse_util(self, previous, current):
        if not current.next:
            current.next = previous
            return current

        new_head = self.reverse_util(current, current.next)
        current.next = previous

        return new_head

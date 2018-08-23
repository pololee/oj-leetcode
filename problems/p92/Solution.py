class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse_between(self, head, m, n):
        if not head or not head.next or m == n:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head

        # anchor is node at m - 1 position
        anchor = dummy_head
        for _ in range(m - 1):
            anchor = anchor.next
        
        start = anchor.next
        then = start.next

        # Remove then and put it between anchor and anchor.next
        # When start moved to position n, the loop finishes.
        # start was in position m, needs n - m steps to move to position n.
        # visually, start and start.next(the updated then) are moving together
        # the value of the start doesn't change. It's the same node and being pushed
        # further back in every step here.
        for _ in range(n - m):
            start.next = then.next
            then.next = anchor.next
            anchor.next = then
            then = start.next

        return dummy_head.next
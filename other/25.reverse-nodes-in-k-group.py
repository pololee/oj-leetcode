# ### [25\. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

# Difficulty: **Hard**


# Given a linked list, reverse the nodes of a linked list _k_ at a time and return its modified list.

# _k_ is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of _k_ then left-out nodes in the end should remain as it is.

# **Example:**

# Given this linked list: `1->2->3->4->5`

# For _k_ = 2, you should return: `2->1->4->3->5`

# For _k_ = 3, you should return: `3->2->1->4->5`

# **Note:**

# *   Only constant extra memory is allowed.
# *   You may not alter the values in the list's nodes, only nodes itself may be changed.


# #### Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        tail = self.kTail(prev, k)
        
        while tail:
            nextPrev = prev.next
            
            # prev: dummy
            # tail: 3
            # prev.next: 1
            # dummy->1->2->3->4
            # dummy->2->3->4 # prev.next = temp.next
            # dummy->2->3->1->4 # temp.next = tail.next, tail.next = temp
            # prev.next: 2
            # dummy->3->1->4 # prev.next = temp.next
            # dummy->3->2->1->4 # temp.next = tail.next, tail.next = temp
            # prev.next == tail (both are 3)
            while prev.next != tail:
                temp = prev.next # cache
                prev.next = temp.next # remove
                temp.next = tail.next
                tail.next = temp # insert
            
            tail = self.kTail(nextPrev, k)
            prev = nextPrev
            
        return dummy.next
    
    
    def kTail(self, prev, k):
        curr, cnt = prev, 0
        
        while cnt < k:
            if not curr:
                break

            curr, cnt = curr.next, cnt + 1

        return curr
        
# ### [86\. Partition List](https://leetcode.com/problems/partition-list/)

# Difficulty: **Medium**


# Given a linked list and a value _x_, partition it such that 
# all nodes less than _x_ come before nodes greater than or equal to _x_.

# You should preserve the original relative order of the nodes in each of the two partitions.

# **Example:**

# ```
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# ```


# #### Solution

# Language: **Python3**

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        smallDummy = ListNode(-1)
        bigDummy = ListNode(-1)
        small, big, curr = smallDummy, bigDummy, head
        
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next
            
            curr = curr.next
        
        big.next = None
        small.next = bigDummy.next
        
        return smallDummy.next
        
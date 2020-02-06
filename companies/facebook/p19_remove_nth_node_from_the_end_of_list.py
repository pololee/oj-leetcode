# ### [19\. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

# Difficulty: **Medium**


# Given a linked list, remove the _n_-th node from the end of list and return its head.

# **Example:**

# ```
# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# ```

# **Note:**

# Given _n_ will always be valid.

# **Follow up:**

# Could you do this in one pass?


# #### Solution

# Language: **Python3**

# ```python3
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# ​
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or n <= 0:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        first, second = dummy, dummy
        step = 0
        while first and step <= n:
            first = first.next
            step += 1
        
        if not first and step < n + 1:
            return head
        
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    print(sol.removeNthFromEnd(head, 1))

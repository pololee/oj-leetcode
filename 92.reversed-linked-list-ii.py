# ### [92\. Reverse Linked List IICopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/reverse-linked-list-ii/)

# Difficulty: **Medium**


# Reverse a linked list from position _m_ to _n_. Do it in one-pass.

# **Note: **1 ≤ _m_ ≤ _n_ ≤ length of list.

# **Example:**

# ```
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# ```


# #### Solution

# Language: **Python3**

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        anchor = dummy_head
        for _ in range(m - 1):
            anchor = anchor.next
        
        start = anchor.next
        then = start.next
        
        self.printList(dummy_head.next)
        for _ in range(n - m):
            print("start: {}, then: {}, archor: {}".format(start.val, then.val, anchor.val))
            start.next = then.next # remove then

            then.next = anchor.next
            anchor.next = then # put then after anchor

            then = start.next
            self.printList(dummy_head.next)
            print("start: {}, then: {}, archor: {}".format(start.val, then.val, anchor.val))
        return dummy_head.next
    
    def printList(self, head):
        ans = []
        while head:
            ans.append(str(head.val))
            head = head.next
        
        print("->".join(ans))

if __name__ == "__main__":
    dummy = ListNode(0)
    curr = dummy
    for i in range(1, 6):
        curr.next = ListNode(i)
        curr = curr.next
    head = dummy.next
    sol = Solution()
    sol.reverseBetween(head, 2, 4)

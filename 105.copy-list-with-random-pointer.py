"""
Definition for singly-linked list with a random pointer.

"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None

        originalToCopy = dict()
        dummyHead = RandomListNode(-1)
        dummyCurr = dummyHead
        curr = head

        while curr:
            dummyCurr.next = RandomListNode(curr.label)
            originalToCopy[id(curr)] = dummyCurr.next

            curr = curr.next
            dummyCurr = dummyCurr.next

        curr = head
        copyCurr = dummyHead.next

        while curr:
            if curr.random:
                copyCurr.random = originalToCopy[id(curr.random)]
            curr = curr.next
            copyCurr = copyCurr.next

        return dummyHead.next


class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def copyNext(self, head):
        curr = head
        while curr:
            copy = RandomListNode(curr.label)
            copy.random = curr.random
            copy.next = curr.next
            curr.next = copy
            curr = curr.next.next

    def copyRandom(self, head):
        curr = head
        while curr:
            copy = curr.next
            if copy.random:
                copy.random = curr.random.next

            curr = curr.next.next

    def splitList(self, head):
        newHead = head.next
        curr = head
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next
            if copy.next:
                copy.next = copy.next.next
        
        return newHead

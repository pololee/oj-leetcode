import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def partition(self, head, target):
        if not head:
            return (None, None)
        smallDummy = Node(-1)
        bigDummy = Node(-1)
        small, big, curr = smallDummy, bigDummy, head

        while curr:
            if curr.val < target:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next

            curr = curr.next

        small.next = None
        big.next = None

        return (smallDummy.next, bigDummy.next)

    def sortLinkedList(self, head):
        if not head:
            return head

        smallHead, bigHead = self.partition(head.next, head.val)
        bigHead = self.sortLinkedList(bigHead)

        if smallHead:
            ans = self.sortLinkedList(smallHead)
            curr = ans
            while curr.next:
                curr = curr.next

            curr.next = head
            head.next = bigHead

            return ans

        head.next = bigHead
        return head

    def printList(self, head):
        buf = []
        while head:
            buf.append(str(head.val))
            head = head.next

        print("->".join(buf))


class SolutionTest(unittest.TestCase):
    def buildList(self, values):
        dummy = Node(-1)
        curr = dummy

        for i in values:
            curr.next = Node(i)
            curr = curr.next

        return dummy.next

    def testSort(self):
        sol = Solution()

        t1 = [1, 2, 3, 4, 5]
        head = self.buildList(t1)
        sol.printList(sol.sortLinkedList(head))

        t2 = [5, 4, 3, 2, 1]
        head = self.buildList(t2)
        sol.printList(sol.sortLinkedList(head))

        t3 = [1, 3, 2, 4, 5]
        head = self.buildList(t3)
        sol.printList(sol.sortLinkedList(head))


if __name__ == "__main__":
    unittest.main()

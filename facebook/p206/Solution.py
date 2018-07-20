class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        The most important thing to this question is TWO pointers. Prev and Current
        """
        previous = None
        current = head
        while current:
            nextTmp = current.next
            current.next = previous
            previous = current
            current = nextTmp
        return previous
    
    def reverse_list_recursive(self, head):
        if not head or not head.next:
            return head
        reverse_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return reverse_head

def create_dummy_list():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(0)
    a.next = b
    b.next = c
    c.next = d

    return a

def print_list(head):
    current = head
    if not current:
        return None
    print("{} ".format(current.val), end="")
    current = current.next
    while current:
        print("-> {}".format(current.val), end=" ")
        current = current.next
    print("\n")

def main():
    dummy_list = create_dummy_list()
    print("Original List")
    print_list(dummy_list)

    sol = Solution()
    new_head = sol.reverse_list(dummy_list)
    print_list(new_head)

    dummy_list = create_dummy_list()
    new_head = sol.reverse_list_recursive(dummy_list)
    print_list(new_head)

if __name__ == '__main__':
    main()

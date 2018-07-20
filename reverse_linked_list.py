class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(previous, current):
    if not current.next:
        current.next = previous
        return current
    
    new_head = reverse(current, current.next)
    current.next = previous

    return new_head



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    new_head = reverse(None, head)
    print(new_head.val)
    print(new_head.next.val)
    print(new_head.next.next.val)
    print(new_head.next.next.next.val)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.table = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.table:
            return -1

        node = self.table[key]
        self.remove(node)
        self.addToTail(node)

        return node.value
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if self.get(key) != -1:
            self.table[key].value = value
            return

        if len(self.table) == self.capacity:
            node = self.head.next
            del self.table[node.key]
            self.remove(node)

        toInsert = Node(key, value)
        self.table[key] = toInsert
        self.addToTail(toInsert)

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addToTail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail

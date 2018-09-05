class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.end = None
        self.table = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1

        node = self.table[key]
        self.remove(node)
        self.setHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            node = self.table[key]
            node.value = value
            self.remove(node)
            self.setHead(node)
        else:
            if len(self.table) >= self.capacity:
                del self.table[self.end.key]
                self.remove(self.end)

            node = Node(key, value)
            self.table[key] = node
            self.setHead(node)

    def remove(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.end = node.prev
        else:
            node.next.prev = node.prev

    def setHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        if self.end is None:
            self.end = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

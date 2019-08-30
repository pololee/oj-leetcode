# ### [622\. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

# Difficulty: **Medium**


# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Your implementation should support following operations:

# *   `MyCircularQueue(k)`: Constructor, set the size of the queue to be k.
# *   `Front`: Get the front item from the queue. If the queue is empty, return -1.
# *   `Rear`: Get the last item from the queue. If the queue is empty, return -1.
# *   `enQueue(value)`: Insert an element into the circular queue. Return true if the operation is successful.
# *   `deQueue()`: Delete an element from the circular queue. Return true if the operation is successful.
# *   `isEmpty()`: Checks whether the circular queue is empty or not.
# *   `isFull()`: Checks whether the circular queue is full or not.

# **Example:**

# ```
# MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
# circularQueue.enQueue(1);  // return true
# circularQueue.enQueue(2);  // return true
# circularQueue.enQueue(3);  // return true
# circularQueue.enQueue(4);  // return false, the queue is full
# circularQueue.Rear();  // return 3
# circularQueue.isFull();  // return true
# circularQueue.deQueue();  // return true
# circularQueue.enQueue(4);  // return true
# circularQueue.Rear();  // return 4
# ```

# **Note:**

# *   All values will be in the range of [0, 1000].
# *   The number of operations will be in the range of [1, 1000].
# *   Please do not use the built-in Queue library.


# #### Solution
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.cnt = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cnt == self.size:
            return False

        node = Node(value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        self.cnt += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cnt == 0:
            return False

        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cnt -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.cnt == 0:
            return -1

        return self.head.next.val

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.cnt == 0:
            return -1

        return self.tail.prev.val

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cnt == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cnt == self.size


class MyCircularQueue2:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.cnt = 0
        self.front = 0
        self.rear = -1
        self.arry = [0 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.size
        self.arry[self.rear] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.size
        self.cnt -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arry[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arry[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.cnt == self.size

    # Your MyCircularQueue object will be instantiated and called as such:
    # obj = MyCircularQueue(k)
    # param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()

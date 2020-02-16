class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.minStack:
            self.minStack.append(min(x, self.minStack[-1]))
        else:
            self.minStack.append(x)

        self.mainStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.minStack.pop()
        self.mainStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

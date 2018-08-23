import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)

    def minimum(self):
        return self.heap[0]


class MaxCompareWrapper:
    def __init__(self, x):
        self.val = x

    def __lt__(self, other):
        return self.val > other.val

    def value(self):
        return self.val


class MaxHeap(MinHeap):
    def push(self, item):
        heapq.heappush(self.heap, MaxCompareWrapper(item))

    def pop(self):
        return heapq.heappop(self.heap).value()

    def maximum(self):
        return self.heap[0].value()


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low_max_heap = MaxHeap()
        self.high_min_heap = MinHeap()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.low_max_heap.push(num)
        self.high_min_heap.push(self.low_max_heap.pop())

        if self.high_min_heap.size() > self.low_max_heap.size():
            self.low_max_heap.push(self.high_min_heap.pop())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.low_max_heap.size() == 0 and self.high_min_heap.size() == 0:
            return 0.0

        if self.low_max_heap.size() == self.high_min_heap.size():
            return (self.low_max_heap.maximum() + self.high_min_heap.minimum()) / 2
        else:
            return self.low_max_heap.maximum() * 1.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def main():
    min_heap = MinHeap()
    test = [5, 7, 9, 1, 3]
    for i in test:
        min_heap.push(i)
    print(min_heap.min_heap)
    print(min_heap.minimum())
    while min_heap.size() > 0:
        print(min_heap.pop())

    max_heap = MaxHeap()
    for i in test:
        max_heap.push(i)
    print(list(map(lambda x:x.val, max_heap.max_heap)))
    print(max_heap.maximum())
    while max_heap.size() > 0:
        print(max_heap.pop())

if __name__ == '__main__':
    main()

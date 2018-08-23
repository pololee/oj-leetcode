# https: // www.cs.cmu.edu/~adamchik/15-121/lectures/Binary % 20Heaps/heaps.html
# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Binary%20Heaps/code/Heap.java


class MinHeap:
    """
    The value of each node is >= the value of its parent
    The min value is at the root
    """

    def __init__(self, array=[]):
        # import to use list(), check https://docs.python-guide.org/writing/gotchas/
        self.heap = list(array)
        if len(self.heap) > 1:
            self.build_heap()

    def build_heap(self):
        last_parent = (len(self.heap) - 2) // 2
        for i in reversed(range(last_parent + 1)):
            self.sift_down(i)

    def insert(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)

    def delete_min(self):
        if len(self.heap) == 0:
            raise Exception("heap is empty.")

        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)
        return minimum

    def sift_up(self, k):
        if k < 0 or k >= len(self.heap):
            return
        tmp = self.heap[k]

        while (k-1) // 2 >= 0:
            parent = (k-1) // 2

            if self._greater(self.heap[parent], tmp):
                self.heap[k] = self.heap[parent]
            else:
                break
            k = parent

        self.heap[k] = tmp

    def sift_down(self, k):
        if k < 0 or k >= len(self.heap):
            return
        tmp = self.heap[k]
        size = len(self.heap)

        while 2 * k + 1 < size:
            child = 2 * k + 1

            # pick the smaller child
            if child < size - 1 and self._greater(self.heap[child], self.heap[child+1]):
                child += 1
            if self._greater(tmp, self.heap[child]):
                self.heap[k] = self.heap[child]
            else:
                break
            k = child
        self.heap[k] = tmp

    def _greater(self, a, b):
        return a > b


def main():
    test = [6, 7, 12, 10, 15, 17]
    test_heap = MinHeap(test)
    print(test_heap.heap)
    test_heap.insert(5)
    print(test_heap.heap)

    test = [3, 1, 6, 5, 2, 4]
    print(test)
    test_heap2 = MinHeap(test)
    print(test_heap2.heap)
    for _ in range(len(test)):
        print("min: {}".format(test_heap2.delete_min()))
        print("heap: {}".format(test_heap2.heap))

# expected output:
#
# [6, 7, 12, 10, 15, 17]
# [5, 7, 6, 10, 15, 17, 12]
# [3, 1, 6, 5, 2, 4]
# [1, 2, 4, 5, 3, 6]
# min: 1
# heap: [2, 3, 4, 5, 6]
# min: 2
# heap: [3, 5, 4, 6]
# min: 3
# heap: [4, 5, 6]
# min: 4
# heap: [5, 6]
# min: 5
# heap: [6]
# min: 6
# heap: []


if __name__ == '__main__':
    main()

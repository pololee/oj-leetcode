class MaxHeap:
    """
    the value of each node is less than or equal to the value of its parent
    with the maximum value at the root
    """

    def __init__(self, array=[]):
        self.heap = list(array)
        if len(self.heap) > 1:
            self.build_heap()

    def build_heap(self):
        # (last_index - 1) // 2
        last_parent = (len(self.heap) - 2) // 2
        for i in reversed(range(last_parent + 1)):
            self.sift_down(i)

    def insert(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            raise Exception("heap is empty.")

        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)
        return maximum

    def sift_up(self, k):
        if k < 0 or k >= len(self.heap):
            return

        tmp = self.heap[k]
        while (k - 1) // 2 >= 0:
            parent = (k - 1) // 2

            if self._smaller(self.heap[parent], tmp):
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

            # pick the bigger child
            if child < size - 1 and self._smaller(self.heap[child], self.heap[child+1]):
                child += 1
            if self._smaller(tmp, self.heap[child]):
                self.heap[k] = self.heap[child]
            else:
                break
            k = child
        self.heap[k] = tmp

    def _smaller(self, a, b):
        return a < b

def main():
    test = [3, 1, 6, 5, 2, 4, 7]
    test_heap = MaxHeap(test)
    print(test_heap.heap)
    for _ in range(len(test)):
        print("max: {}".format(test_heap.delete_max()))
        print("heap: {}".format(test_heap.heap))

if __name__ == '__main__':
    main()

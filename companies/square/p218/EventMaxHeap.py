from Event import Event
from IPython import embed

class EventMaxHeap:
    def __init__(self, size):
        self.heapIdx = [-1 for _ in range(size)]
        # heapIdx[i]
        # represent building[i]'s idx in heap
        self.heap = list()

    def add(self, event):
        self.heap.append(event)
        self.heapIdx[event.id] = len(self.heap) - 1
        self.sift_up(self.heapIdx[event.id])

    def max_height(self):
        if self.heap:
            return self.heap[0].height
        return 0

    def delete_building(self, event_id):
        if self.heapIdx[event_id] == -1 or not self.heap:
            return

        event_heap_idx = self.heapIdx[event_id]
        last_event_idx = len(self.heap) - 1
        self.swap(event_heap_idx, last_event_idx)

        del self.heap[-1]
        self.heapIdx[event_id] = -1

        self.sift_up(event_heap_idx)
        self.sift_down(event_heap_idx)

    def sift_up(self, k):
        if k < 0 or k >= len(self.heap):
            return

        while (k-1) // 2 >= 0:
            parent = (k - 1) // 2

            if self._smaller(parent, k):
                self.swap(parent, k)
            else:
                break
            k = parent

    def sift_down(self, k):
        if k < 0 or k >= len(self.heap):
            return

        size = len(self.heap)
        while 2 * k + 1 < size:
            child = 2 * k + 1

            if child < size - 1 and self._smaller(child, child + 1):
                child += 1

            if self._smaller(k, child):
                self.swap(k, child)
            else:
                break
            k = child

    def _smaller(self, aidx, bidx):
        return self.heap[aidx].height < self.heap[bidx].height

    def swap(self, aidx, bidx):
        event_a = self.heap[aidx]
        event_b = self.heap[bidx]

        self.heap[aidx] = event_b
        self.heap[bidx] = event_a

        self.heapIdx[event_a.id] = bidx
        self.heapIdx[event_b.id] = aidx


def main():
    e1 = Event(0, 0, 3, Event.ENTERING)
    e2 = Event(1, 0, 1, Event.ENTERING)
    e3 = Event(2, 0, 6, Event.ENTERING)
    e4 = Event(3, 0, 5, Event.ENTERING)

    heap = EventMaxHeap(4)
    heap.add(e1)
    heap.add(e2)
    heap.add(e3)
    heap.add(e4)

if __name__ == '__main__':
    main()

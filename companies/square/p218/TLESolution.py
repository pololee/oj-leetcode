class Event:
    def __init__(self, building_id, x, height, entering):
        self.id = building_id
        self.x = x
        self.height = height
        self.entering = entering
        self.leaving = not entering

    def __eq__(self, other):
        return self.x == other.x and self.height == other.height and self.entering == other.entering

    def __lt__(self, other):
        if self.x == other.x:
            # overlap at the boundry
            # both entering: process the highest first
            # both leaving: process the lowest first
            # entering and leaving: always processing entering first
            if self.entering and other.entering:
                return self.height > other.height
            elif self.leaving and other.leaving:
                return self.height < other.height
            else:
                return self.entering
        return self.x < other.x

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "id: {}, x: {}, height: {}, entering: {}".format(self.id, self.x, self.height, self.entering)


class SomeDataStruct:
    def __init__(self):
        self.heap = []

    def add(self, event):
        self.heap.append(event)

    def max(self):
        if self.heap:
            event = max(self.heap, key=lambda x: x.height)
            return event.height
        return 0

    def remove(self, event):
        for idx, x in enumerate(self.heap):
            if x.id == event.id:
                del self.heap[idx]


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = self.buildings_to_events(buildings)
        # print('\n'.join(map(lambda event: str(event), events)))
        ds = SomeDataStruct()
        key_points = []

        for event in events:
            # print(str(event))
            if event.entering:
                if event.height > ds.max():
                    key_points.append([event.x, event.height])
                ds.add(event)

            if event.leaving:
                ds.remove(event)
                if event.height > ds.max():
                    key_points.append([event.x, ds.max()])
            # print(list(map(lambda x: x.height, ds.heap)))
        return key_points

    def buildings_to_events(self, buildings):
        events = list()
        for idx, building in enumerate(buildings):
            left, right, height = building
            events.append(Event(idx, left, height, True))
            events.append(Event(idx, right, height, False))
        events.sort()
        return events


def main():
    sol = Solution()
    buildings = [[2, 9, 10], [3, 7, 15],
                 [5, 12, 12], [15, 20, 10],
                 [19, 24, 8]]
    # print(sol.getSkyline(buildings))
    buildings = [[2, 5, 10], [5, 8, 10]]
    # print(sol.getSkyline(buildings))
    buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
    buildings = [[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]]
    print(sol.getSkyline(buildings))

# expected output
# id: 0, x: 2, height: 10, entering: True
# [10]
# id: 1, x: 3, height: 15, entering: True
# [10, 15]
# id: 2, x: 5, height: 12, entering: True
# [10, 15, 12]
# id: 1, x: 7, height: 15, entering: False
# [10, 12]
# id: 0, x: 9, height: 10, entering: False
# [12]
# id: 2, x: 12, height: 12, entering: False
# []
# id: 3, x: 15, height: 10, entering: True
# [10]
# id: 4, x: 19, height: 8, entering: True
# [10, 8]
# id: 3, x: 20, height: 10, entering: False
# [8]
# id: 4, x: 24, height: 8, entering: False
# []
# [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
#
# id: 0, x: 2, height: 10, entering: True
# [10]
# id: 1, x: 5, height: 10, entering: True
# [10, 10]
# id: 0, x: 5, height: 10, entering: False
# [10]
# id: 1, x: 8, height: 10, entering: False
# []
# [[2, 10], [8, 0]]

if __name__ == '__main__':
    main()

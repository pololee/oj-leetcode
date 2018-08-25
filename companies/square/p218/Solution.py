from Event import Event
from EventMaxHeap import EventMaxHeap
from IPython import embed


class FinalSolution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = self.buildings_to_events(buildings)
        max_heap = EventMaxHeap(size=len(buildings))
        key_points = list()

        for event in events:
            if event.entering():
                if event.height > max_heap.max_height():
                    key_points.append([event.x, event.height])
                max_heap.add(event)

            if event.leaving():
                max_heap.delete_building(event_id=event.id)
                if event.height > max_heap.max_height():
                    key_points.append([event.x, max_heap.max_height()])
        return key_points

    def buildings_to_events(self, buildings):
        events = list()

        for idx, building in enumerate(buildings):
            left, right, height = building
            events.append(Event(idx, left, height, Event.ENTERING))
            events.append(Event(idx, right, height, Event.LEAVING))
        events.sort()

        return events


def main():
    sol = FinalSolution()
    buildings = [[2, 9, 10], [3, 7, 15],
                 [5, 12, 12], [15, 20, 10],
                 [19, 24, 8]]
    # events = sol.buildings_to_events(buildings)
    key_points = sol.getSkyline(buildings)


if __name__ == '__main__':
    main()

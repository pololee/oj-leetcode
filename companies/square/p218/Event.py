# from IPython import embed

class Event:
    ENTERING = 1
    LEAVING = -1

    def __init__(self, eid, x, height, etype):
        self.id = eid
        self.x = x
        self.height = height
        self.type = etype

    def entering(self):
        return self.type == self.ENTERING

    def leaving(self):
        return self.type == self.LEAVING

    # three cases:
    # both entering: process higher first
    # both leaving: process lower first
    # leaving and entering: always process entering first
    def __lt__(self, other):
        if self.x == other.x:
            if self.entering() and other.entering():
                return self.height > other.height
            elif self.leaving() and other.leaving():
                return self.height < other.height
            else:
                return self.entering()
        return self.x < other.x

    def __str__(self):
        return "id: {}, x: {}, height: {}, type: {}".format(self.id, self.x, self.height, self.type)

def main():
    buildings = [[2, 9, 10], [3, 7, 15],
                [5, 12, 12], [15, 20, 10],
                [19, 24, 8]]
    events = list()
    for idx, building in enumerate(buildings):
        left, right, height = building
        events.append(Event(idx, left, height, Event.ENTERING))
        events.append(Event(idx, right, height, Event.LEAVING))
    events.sort()
    print('\n'.join((map(lambda x: str(x), events))))
# Expected output:
# id: 0, x: 2, height: 10, type: 1
# id: 1, x: 3, height: 15, type: 1
# id: 2, x: 5, height: 12, type: 1
# id: 1, x: 7, height: 15, type: -1
# id: 0, x: 9, height: 10, type: -1
# id: 2, x: 12, height: 12, type: -1
# id: 3, x: 15, height: 10, type: 1
# id: 4, x: 19, height: 8, type: 1
# id: 3, x: 20, height: 10, type: -1
# id: 4, x: 24, height: 8, type: -1

if __name__ == '__main__':
    main()

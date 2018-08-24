class TestSort:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        return self.x < other.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def main():
    arry = []
    arry.append(TestSort(1, 2))
    arry.append(TestSort(2, 1))
    arry.append(TestSort(2, 2))
    arry.append(TestSort(2, 3))
    arry.append(TestSort(0, 2))
    arry.sort()
    print(arry)


# expected [(0, 2), (1, 2), (2, 3), (2, 2), (2, 1)]
if __name__ == '__main__':
    main()

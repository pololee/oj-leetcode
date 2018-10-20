import unittest
from collections import deque


class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        if not routes or not routes[0]:
            return -1

        table = self.stopBoard(routes)
        if S not in table or T not in table:
            return -1

        ret = 0
        busTaken = set()
        queue = deque()
        queue.append(S)
        while queue:
            ret += 1

            size = len(queue)
            for _ in range(size):
                currStop = queue.popleft()
                buses = table[currStop]
                for bus in buses:
                    if bus in busTaken:
                        continue
                    busTaken.add(bus)
                    for stop in routes[bus]:
                        if stop == T:
                            return ret
                        queue.append(stop)
            ret += 1
        return -1

    def stopBoard(self, routes):
        table = dict()  # key is bus stop, value is a list of buses that go though the list
        numOfBuses = len(routes)
        for busIdx in range(numOfBuses):
            for stop in routes[busIdx]:
                if stop not in table:
                    table[stop] = list()
                table[stop].append(busIdx)
        return table


class TestSolution(unittest.TestCase):
    sol = Solution()

    def testNumBusesToDestination(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        self.assertEqual(2, self.sol.numBusesToDestination(routes, S, T))


if __name__ == '__main__':
    unittest.main()

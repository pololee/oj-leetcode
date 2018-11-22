import random


class Solution:
    def __init__(self):
        self.table = dict()
        self.values = []
        self.uniqueCounter = dict()
        self.uniqueValues = []

    def put(self, key, value):
        if key in self.table:
            _, idx = self.table[key]
            self.table[key] = (value, idx)
            self.values[idx] = (value, key)
        else:
            size = len(self.values)
            self.table[key] = (value, size)
            self.values.append((value, key))

        if value in self.uniqueCounter:
            cnt, idx = self.uniqueCounter[value]
            self.uniqueCounter[value] = (cnt + 1, idx)
        else:
            size = len(self.uniqueValues)
            self.uniqueCounter[value] = (1, size)
            self.uniqueValues.append(value)

    def get(self, key):
        if key not in self.table:
            return -1
        return self.table[key][0]

    def delete(self, key):
        if key not in self.table:
            return

        value, idx = self.table[key]
        del self.table[key]
        if idx < len(self.values) - 1:
            self.values[idx], self.values[-1] = self.values[-1], self.values[idx]
            movedValue, movedKey = self.values[idx]
            self.table[movedKey] = (movedValue, idx)

        cnt, uIdx = self.uniqueCounter[value]
        newCnt = cnt - 1
        if newCnt == 0:
            del self.uniqueCounter[value]
            if uIdx < len(self.uniqueValues) - 1:
                self.uniqueValues[uIdx], self.uniqueValues[-1] = self.uniqueValues[-1], self.uniqueValues[uIdx]
                movedValue = self.uniqueValues[uIdx]
                tmpCnt, _ = self.uniqueCounter[movedValue]
                self.uniqueCounter[movedValue] = (tmpCnt, uIdx)
        else:
            self.uniqueCounter[value] = (newCnt, uIdx)

    def get_random_value(self):
        size = len(self.table)
        idx = random.randint(0, size - 1)
        return self.values[idx][0]

    def get_random_unique_value(self):
        size = len(self.uniqueCounter)
        idx = random.randint(0, size - 1)
        return self.uniqueValues[idx]

    def random_experiment(self):
        fiveCnt = 0
        sixCnt = 0
        for _ in range(100):
            val = self.get_random_value()
            if val == 5:
                fiveCnt += 1
            elif val == 6:
                sixCnt += 1
        print("five: {}, six: {}".format(fiveCnt, sixCnt))

    def unique_random_experiment(self):
        fiveCnt = 0
        sixCnt = 0
        for _ in range(100):
            val = self.get_random_unique_value()
            if val == 5:
                fiveCnt += 1
            elif val == 6:
                sixCnt += 1
        print("five: {}, six: {}".format(fiveCnt, sixCnt))


if __name__ == "__main__":
    sol = Solution()
    sol.put("a", 5)
    sol.put("b", 5)
    sol.put("c", 6)
    sol.put("d", 5)
    # print(sol.table)
    # print(sol.values)

    # sol.random_experiment()
    # sol.delete("d")
    # print(sol.table)
    # print(sol.values)
    # sol.random_experiment()
    # sol.delete("c")
    # print(sol.table)
    # print(sol.values)
    # sol.random_experiment()
    print(sol.uniqueCounter)
    print(sol.uniqueValues)
    sol.unique_random_experiment()
    sol.delete("d")
    print(sol.uniqueCounter)
    print(sol.uniqueValues)
    sol.unique_random_experiment()
    sol.delete("c")
    print(sol.uniqueCounter)
    print(sol.uniqueValues)
    sol.unique_random_experiment()

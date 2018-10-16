import math
import unittest


class PriceWrap:
    def __init__(self, idx, price):
        self.idx = idx
        self.price = price
        self.floorPrice = math.floor(price)
        self.floorDiffAbs = abs(self.price - self.floorPrice)
        self.ceilPrice = math.ceil(price)
        self.ceilDiffAbs = abs(self.ceilPrice - self.price)


class RoundPrices:
    def roundUp(self, array):
        if not array:
            return []

        target = round(sum(array))
        wrappedArray = [PriceWrap(idx, price)
                        for idx, price in enumerate(array)]

        floorSum = sum([x.floorPrice for x in wrappedArray])
        floorDiff = target - floorSum

        if floorDiff == 0:
            return [math.floor(x) for x in array]

        ceilSum = sum(map(lambda x: x.ceilPrice, wrappedArray))
        ceilDiff = ceilSum - target
        if ceilDiff == 0:
            return [math.ceil(x) for x in array]

        if floorDiff <= ceilDiff:
            return self.pickFloor(array, wrappedArray, floorDiff)

        return self.pickCeil(array, wrappedArray, ceilDiff)

    def pickFloor(self, array, wrappedArray, diff):
        ans = [math.floor(x) for x in array]

        sortByCeillDiff = sorted(
            filter(lambda x: x.ceilDiffAbs != 0, wrappedArray),
            key=lambda x: x.ceilDiffAbs
        )
        for wrap in sortByCeillDiff[:diff]:
            ans[wrap.idx] += 1

        return ans

    def pickCeil(self, array, wrappedArray, diff):
        ans = [math.ceil(x) for x in array]

        sortByFloorDiff = sorted(
            filter(lambda x: x.floorDiffAbs != 0, wrappedArray),
            key=lambda x: x.floorDiffAbs
        )
        for wrap in sortByFloorDiff[:diff]:
            ans[wrap.idx] -= 1

        return ans


class SolutionTest(unittest.TestCase):
    sol = RoundPrices()

    def testRoundUp(self):
        test = [1.2, 2.3, 3.4]
        self.assertEqual([1, 2, 4], self.sol.roundUp(test))
        test = [-2, -1.2, -1.4]
        self.assertEqual([-2, -1, -2], self.sol.roundUp(test))
        test = [1.4, 1.7, 1.6]
        self.assertEqual([1, 2, 2], self.sol.roundUp(test))

if __name__ == '__main__':
    unittest.main()

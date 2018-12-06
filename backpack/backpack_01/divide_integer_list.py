# given a list of integer,
# how to divide them into two sub list, so that the sum of them are closest to
# each other

# Think this as 01 backpack problem
# Let M be the total sum of the original list
# Now the pack total capacity is M / 2
# items are the list of integer, now try to fill this pack as much as possible
import unittest


class Solution:
    def equalDivide(self, nums):
        if not nums:
            return []

        totalSum = sum(nums)
        capacity = totalSum // 2
        # print(capacity)
        size = len(nums)
        DP = [[0 for _ in range(capacity + 1)] for _ in range(size + 1)]

        for i in range(1, size + 1):
            for j in range(1, capacity + 1):
                num = nums[i-1]

                if num > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i-1][j-num] + num)
        aGroup = []
        bGroup = []
        i = size
        j = capacity

        while i > 0 and j > 0:
            num = nums[i-1]
            if DP[i-1][j] == DP[i][j]:
                aGroup.append(num)
            else:
                bGroup.append(num)
                j -= num
            i -= 1

        return [aGroup, bGroup]


class SolutionTest(unittest.TestCase):
    def testEqualDivide(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 6]
        print(sol.equalDivide(nums))


if __name__ == "__main__":
    unittest.main()

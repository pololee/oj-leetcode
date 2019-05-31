# https://www.youtube.com/watch?v=LPFhl65R7ww
from typing import List
import sys


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)

        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, x

        while left <= right:
            partitionX = left + (right - left) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = - \
                sys.maxsize if partitionX == 0 else nums1[partitionX - 1]
            minRightX = sys.maxsize if partitionX == x else nums1[partitionX]

            maxLeftY = - \
                sys.maxsize if partitionY == 0 else nums2[partitionY - 1]
            minRightY = sys.maxsize if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 3], [2, 4]))

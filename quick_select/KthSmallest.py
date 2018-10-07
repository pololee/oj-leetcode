class KthSmallest:
    def kthSmallest(self, k, nums):
        if not nums or k < 1 or k > len(nums):
            return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            storeIndex = self.partition(nums, low, high)

            if storeIndex == k - 1:
                return nums[storeIndex]
            elif storeIndex < k - 1:
                low = storeIndex + 1
            else:
                high = storeIndex - 1

        return -1

    def partition(self, nums, start, end):
        pivotValue = nums[end]

        storeIndex = start
        for i in range(start, end):
            if nums[i] < pivotValue:
                self.swap(nums, i, storeIndex)
                storeIndex += 1

        self.swap(nums, storeIndex, end)
        return storeIndex

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


def main():
    select = KthSmallest()
    print(select.kthSmallest(3, [9, 3, 2, 4, 8]))
    print(select.kthSmallest(1, [1, 2, 3, 4, 5]))
    print(select.kthSmallest(2, [1, 2, 3, 4, 5]))
    print(select.kthSmallest(3, [1, 2, 3, 4, 5]))
    print(select.kthSmallest(5, [1, 2, 3, 4, 5]))
    print(select.kthSmallest(6, [1, 2, 3, 4, 5]))
    print(select.kthSmallest(3, [2, 2, 2]))


if __name__ == '__main__':
    main()

class KthLargest:
    def kthLargest(self, k, nums):
        if not nums or k < 1 or k > len(nums):
            return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            storeIndex = self.partition(nums, low, high)

            if storeIndex == k - 1:
                return nums[storeIndex]
            elif storeIndex < k - 1: 
                # if storeIndex < k - 1, means there are < k - 1 values less than nums[storeIndex]
                # the value we look for should fall in [storeIndex + 1, high]
                low = storeIndex + 1
            else:
                high = storeIndex - 1
        return -1

    # we use nums[end] as the pivot value
    # after this function, we will get a storeIndex
    # which is where the pivot value should be
    # that means there are # of storeIndex values less than nums[storeIndex]
    # note it's nums[storeIndex], because the last swap we did in this function
    def partition(self, nums, start, end):
        pivotValue = nums[end]

        storeIndex = start
        for i in range(start, end):
            if nums[i] > pivotValue: # this line decide we are looking for k th largets
                self.swap(nums, i, storeIndex)
                storeIndex += 1

        self.swap(nums, storeIndex, end)
        return storeIndex

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

def main():
    select = KthLargest()
    print(select.kthLargest(3, [9, 3, 2, 4, 8]))
    print(select.kthLargest(1, [1, 2, 3, 4, 5]))
    print(select.kthLargest(2, [1, 2, 3, 4, 5]))
    print(select.kthLargest(3, [1, 2, 3, 4, 5]))
    print(select.kthLargest(5, [1, 2, 3, 4, 5]))
    print(select.kthLargest(6, [1, 2, 3, 4, 5]))
    print(select.kthLargest(3, [2, 2, 2]))

if __name__ == '__main__':
    main()

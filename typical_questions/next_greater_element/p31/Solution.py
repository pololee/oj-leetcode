class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        valley_idx = self.find_valley(nums)
        if valley_idx == -1:
            self.reverse(nums, 0)
        else:
            first_greater_idx = self.first_greater(nums, valley_idx)
            self.swap(nums, valley_idx, first_greater_idx)
            self.reverse(nums, valley_idx + 1)

    def find_valley(self, nums):
        size = len(nums)
        for i in reversed(range(size - 1)):
            if nums[i] < nums[i+1]:
                return i
        return -1

    def first_greater(self, nums, valley_idx):
        target = nums[valley_idx]
        size = len(nums)
        for i in reversed(range(size)):
            if nums[i] > target:
                return i

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

def main():
    sol = Solution()
    test = [1, 2, 3]
    sol.nextPermutation(test)
    print(test)
    test = [3, 2, 1]
    sol.nextPermutation(test)
    print(test)

if __name__ == '__main__':
    main()

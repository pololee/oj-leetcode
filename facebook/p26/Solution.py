class Solution:
    def removeDuplicates(self, nums):
        if not nums or len(nums) < 2:
            return len(nums)
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

if __name__ == '__main__':
    test = [1, 1, 2]
    sol = Solution()
    print(sol.removeDuplicates(test))
    print(test)
    test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.removeDuplicates(test2))
    print(test2)
    test3 = [1, 2, 3]
    print(sol.removeDuplicates(test3))
    print(test3)

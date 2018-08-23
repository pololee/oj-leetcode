class Solution:
    def search(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype int
        """
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            elif nums[mid] < nums[right]:
                # from mid to right, it's ascending
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # from left to mid, it's ascending
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
    def search_2(self, nums, target):
        if not nums:
            return -1
        
        # find the pivot point, check question p153
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = right # when loop terminates, mid == right == left

        left = 0
        right = length - 1
        while left <= high:
            mid = left + (right - left) // 2
            real_mid = (mid + pivot) % length
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    test = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(sol.search(test, target))
    print(sol.search(test, 2))
    print(sol.search(test, 3))

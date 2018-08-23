class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        results = [1 for _ in range(size)]

        productForward = 1
        for i in range(1, size):
            productForward *= nums[i-1]
            results[i] *= productForward
        
        productBackward = 1
        for i in range(size - 2, -1, -1):
            productBackward *= nums[i+1]
            results[i] *= productBackward

        return results

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.sortHelper(A, 0, len(A) - 1)
    
    
    def sortHelper(self, A, first, last):
        if first < last:
            splitIdx = self.partition(A, first, last)
            
            self.sortHelper(A, first, splitIdx - 1)
            self.sortHelper(A, splitIdx + 1, last)
    
    
    def partition(self, nums, first, last):
        pivot = nums[first]
        
        leftIdx = first + 1
        rightIdx = last
        
        done = False
        while not done:
            while leftIdx <= rightIdx and nums[leftIdx] <= pivot:
                leftIdx += 1
            
            while leftIdx <= rightIdx and nums[rightIdx] >= pivot:
                rightIdx -= 1
            
            if rightIdx < leftIdx:
                done = True
            else:
                nums[leftIdx], nums[rightIdx] = nums[leftIdx], nums[rightIdx]
        
        nums[first] = nums[rightIdx]
        nums[rightIdx] = pivot
        
        return rightIdx

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,4,5]
    sol.sortIntegers2(nums)

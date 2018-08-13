class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        size = len(nums)
        # initialize all the value to -1, assume they don't have next greater number
        results = [-1 for _ in range(size)]
        stack = [0]

        # note: because it's circular, we loop to 2 * siz (exclusive)
        # the index = i % size
        for i in range(1, 2 * size):
            idx = i % size

            while stack and nums[stack[-1]] < nums[idx]:
                small_idx = stack.pop()
                results[small_idx] = nums[idx]
            
            stack.append(idx)
        
        return results

def main():
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))  # [2,-1,2]
    print(sol.nextGreaterElements([1, 1, 1]))  # [-1,-1,-1]

if __name__ == '__main__':
    main()

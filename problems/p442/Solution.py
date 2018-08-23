class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []

        size = len(nums)
        for i in range(size):
            idx = abs(nums[i]) - 1

            if nums[idx] < 0:
                results.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        return results

def main():
    sol = Solution()
    test = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDuplicates(test))

if __name__ == '__main__':
    main()

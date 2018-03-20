class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        results = []
        self.recursive_permutes(nums, [], results)
        return results

    def recursive_permutes(self, nums, member, results):
        """
        :type nums: List[int]
        :type member: List[int]
        :type results: List[List[int]]
        """
        print("nums: {}".format(nums))
        print("member: {}".format(member))
        if not nums:
            results.append(member)
        else:
            for i in range(len(nums)):
                self.recursive_permutes(nums[:i] + nums[i+1:], member + [nums[i]], results)

def main():
    sol = Solution()
    test = [1, 2, 3]
    print(sol.permute(test))

if __name__ == '__main__':
    main()

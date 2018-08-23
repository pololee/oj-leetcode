class Solution:
    def max_sub_array_len(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0

        sums = [0] * (len(nums) + 1)
        # sums[0] = 0
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        
        # sums[i] = a[0] + ... + a[i-1] 
        # number of elements is i
        # for j > i
        # sums[j] - sums[i] = a[i] + ... + a[j-1]
        # number of elements is j - i

        answer_len = 0
        mapping = dict()
        for i in range(len(nums) + 1):
            if (sums[i] - k) in mapping:
                answer_len = max(answer_len, i - mapping[sums[i] - k])

            if sums[i] not in mapping:
                mapping[sums[i]] = i

        return answer_len

class BetterSolution:
    def max_sub_array_len(self, nums, k):
        if not nums: return 0

        answer_len = 0
        sum_so_far = 0
        mapping = dic()
        for i in range(len(nums)):
            sum_so_far = sum_so_far + nums[i]

            if sum_so_far == k:
                answer_len = i + 1
            elif (sum_so_far - k) in mapping:
                answer_len = max(answer_len, i - mapping[sum_so_far - k])
            
            # this adding to map has to be after the above check
            # reason:
            # because we want to use sum_so_far and all the "previous" sums to
            # check if there is a match for k. sum_so_far should not be in the
            # "previous" yet, i.e. not the in mapping yet.
            if sum_so_far not in mapping:
                mapping[sum_so_far] = i

        return answer_len

def main():
    sol = Solution()
    test1 = [1, -1, 5, -2, 3]
    print(sol.max_sub_array_len(test1, 3)) # expect 4 [1, -1, 5, -2]
    test2 = [-2, -1, 2, 1]
    print(sol.max_sub_array_len(test2, 1)) # expect 2 [-1, 2]

if __name__ == '__main__':
    main()
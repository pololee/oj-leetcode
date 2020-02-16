class Solution:
    MAXIMUM_32BITS_INTEGER = 0x7fffffff

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = self.convert_to_num_array(n)
        valley_bottom_idx = self.find_valley_bottom(nums)

        if valley_bottom_idx == -1:
            return -1

        first_greater_idx = self.the_first_greater(nums, valley_bottom_idx)
        self.swap(nums, valley_bottom_idx, first_greater_idx)
        self.reverse(nums, valley_bottom_idx + 1)

        answer = 0
        for num in nums:
            answer = answer * 10 + num

        return answer if answer <= self.MAXIMUM_32BITS_INTEGER else -1

    def convert_to_num_array(self, n):
        results = []
        while n != 0:
            results.append(n % 10)
            n = n // 10

        return results[::-1]

    def find_valley_bottom(self, nums):
        size = len(nums)
        for i in reversed(range(size - 1)):
            if nums[i] < nums[i+1]:
                return i

        return -1

    def the_first_greater(self, nums, valley_bottom_idx):
        target = nums[valley_bottom_idx]
        for i in reversed(range(len(nums))):
            if nums[i] > target:
                return i

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1


def main():
    sol = Solution()
    # print(sol.nextGreaterElement(12))
    # print(sol.nextGreaterElement(21))
    # print(sol.nextGreaterElement(1))
    # print(sol.nextGreaterElement(111))
    print(sol.nextGreaterElement(230241))


if __name__ == '__main__':
    main()

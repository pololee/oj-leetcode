class PreviousSmallerNumber:
    def previousSmaller(self, n):
        """
        :type n: int
        :rtype int
        """
        nums = self.convert_to_nums(n)
        peek_idx = self.find_peak(nums)

        if peek_idx == -1:
            return -1
        
        first_smaller_idx = self.first_smaller(nums, peek_idx)
        self.swap(nums, peek_idx, first_smaller_idx)
        self.reverse(nums, peek_idx + 1)

        answer = 0
        for num in nums:
            answer = answer * 10 + num
        return answer
    
    def convert_to_nums(self, n):
        results = []
        while n != 0:
            results.append(n % 10)
            n = n // 10
        
        return results[::-1]
    
    def find_peak(self, nums):
        size = len(nums)
        for i in reversed(range(size - 1)):
            if nums[i] > nums[i+1]:
                return i
        return -1
    
    def first_smaller(self, nums, peek_idx):
        target = nums[peek_idx]
        size = len(nums)
        for i in reversed(range(size)):
            if nums[i] < target:
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
    previous = PreviousSmallerNumber()
    print(previous.previousSmaller(123)) #-1
    print(previous.previousSmaller(14321)) #14312
    print(previous.previousSmaller(14123)) #13421


if __name__ == '__main__':
    main()

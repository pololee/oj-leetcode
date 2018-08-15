class EvenSubarray:
    def subarrays(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype list[list[int]]
        """
        if not nums:
            return []
        
        size = len(nums)
        nums_str = ''.join([str(x) for x in nums])
        substr_set = set()
        for i in range(size):
            odds = 0

            for j in range(i, size):
                if nums[j] % 2 == 1:
                    odds += 1
                
                if odds <= k and nums_str[i:j+1] not in substr_set:
                    substr_set.add(nums_str[i:j+1])
        return len(substr_set)

def main():
    sub = EvenSubarray()
    print(sub.subarrays([1, 2, 3, 4], 1))
    print(sub.subarrays([1, 2, 1, 2], 1))
    print(sub.subarrays([1, 1, 1, 1], 1))

if __name__ == '__main__':
    main()


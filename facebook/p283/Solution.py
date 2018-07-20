class Solution:
    def move_zeros(self, nums):
        if not nums or len(nums) == 0:
            return

        # move all the non-zero numbers to the front
        zero_postion = 0
        for n in nums:
            if n != 0:
                nums[zero_postion] = n
                zero_postion += 1
        
        while zero_postion < len(nums):
            nums[zero_postion] = 0
            zero_postion += 1

def main():
    sol = Solution()
    test = [0, 1, 0, 3, 12]
    print(test)
    sol.move_zeros(test)
    print(test)

if __name__ == '__main__':
    main()
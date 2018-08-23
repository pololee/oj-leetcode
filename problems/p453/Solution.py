class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)

        moves = 0
        for number in nums:
            moves += (number - min_num)
        
        return moves
def main():
    sol = Solution()
    print(sol.minMoves([1, 2, 3]))

if __name__ == '__main__':
    main()

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xor = x ^ y

        # result = 0
        # while xor != 0:
        #     if xor % 2 == 1:
        #         result = result + 1
        #     xor = xor // 2
        
        # return result
        return bin(x ^ y).count('1')

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1, 4))
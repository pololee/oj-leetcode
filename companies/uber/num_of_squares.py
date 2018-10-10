# Any positive integer can be represented as a sum of squares of other integers. Example:
# 1 = 1^2
# 10 = 3^2 + 1^2
# 13 = 3^2 + 2^2

# There are multiple solutions for these integers:
# 9 = 3^2
# 9 = 2^2 + 2^2 + 1^2
# and so on

# Write a function that given a positive integer returns the minimum squares needed:
# eg: 
# Input Output Expl.
# 9	      1      9 = 3^2
# 10      2 
# 10
# 3, 3^2 = 9, 1
# 2
# 
# 13
# 3, 3^2 = 9, 4
# 2, 2^2 = 4, 0
#
# 12
# 3, 3^2 = 9, 3
# 1, 1^2 = 1, 2
# 1, 1^2 = 1, 1
# 1, 1^2 = 1, 0 => 3^2 + 1 + 1 + 1
#
# 12 = 2^2 + 2^2 + 2^2

# 12, root 3
# minNum = 12
# for start in reversed(range(2, root+1)):
#    minNum = min(minNum, 1 + self.minSquares(x - start * start))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

class Solution:
    def minSquares(self, x):
        done = {0 : 0, 1 : 1}
        
        return self.minSquaresUtil(x, done)

    def minSquaresUtil(self, x, done):
        if x in done:
            return done[x]
        
        root = math.floor(math.sqrt(x))
        minNum = x + 1
        for start in reversed(range(1, root+1)):
            minNum = min(minNum, 1 + self.(x - start * start, done))

        done[x] = minNum
        return done[x]

sol = Solution()
# print(sol.numOfSquares(3, 12))
# print(sol.numOfSquares(2, 12))
print(sol.minSquares(9))
print(sol.minSquares(12))
print(sol.minSquares(13))
print(sol.minSquares(25))
print(sol.minSquares(72))
# n => sqrt(n)
# sqrt(n) ^ sqrt(n)
# minSquaresutil(n) => sqrt(n) calls of minSquaresutil
        

#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (31.08%)
# Total Accepted:    298.3K
# Total Submissions: 960K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        board = [[] for _ in range(numRows)]
        rowIdx, direction = 0, 1
        
        for x in s:
            board[rowIdx].append(x)
            if rowIdx == 0:
                direction = 1
            elif rowIdx == numRows - 1:
                direction = -1
            
            rowIdx += direction
        print(board)
        board = [''.join(row) for row in board]
        return ''.join(board)



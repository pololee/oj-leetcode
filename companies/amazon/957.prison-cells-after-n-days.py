# [957\. Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)

# Difficulty: **Medium**


# There are 8 prison cells in a row, and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# *   If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# *   Otherwise, it becomes vacant.

# (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

# We describe the current state of the prison in the following way: `cells[i] == 1` if the `i`-th cell is occupied, else `cells[i] == 0`.

# Given the initial state of the prison, return the state of the prison after `N` days (and `N` such changes described above.)


# **Example 1:**

# ```
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# ```


# **Example 2:**

# ```
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
# ```

# **Note:**

# 1.  `cells.length == 8`
# 2.  `cells[i]` is in `{0, 1}`
# 3.  `1 <= N <= 10^9`

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        table = dict()

        while N > 0:
            stringRep = self.strRep(cells)

            if stringRep in table:
                N = N % (table[stringRep] - N)
            table[stringRep] = N

            if N >= 1:
                N -= 1
                cells = self.nextState(cells)
        return cells

    def strRep(self, cells):
        return "".join([str(x) for x in cells])

    def nextState(self, cells):
        newState = [0 for _ in range(8)]
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                newState[i] = 1
        return newState

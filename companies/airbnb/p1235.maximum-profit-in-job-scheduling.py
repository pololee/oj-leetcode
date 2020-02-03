# ### [1235\. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

# Difficulty: **Hard**


# We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

# You're given the `startTime` , `endTime` and `profit` arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

# If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

# **Example 1:**

# **![](https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png)**

# ```
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# ```

# **Example 2:**

# **![](https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png)**

# ```
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
# ```

# **Example 3:**

# **![](https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png)**

# ```
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
# ```

# **Constraints:**

# *   `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`
# *   `1 <= startTime[i] < endTime[i] <= 10^9`
# *   `1 <= profit[i] <= 10^4`


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         
# ```

from typing import *

class Job:
    def __init__(self, startTime, endTime, profit):
        self.startTime = startTime
        self.endTime = endTime
        self.profit = profit


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not startTime or not endTime or not profit:
            return 0
        
        size = len(profit)
        jobs = [Job(startTime[i], endTime[i], profit[i]) for i in range(size)]
        jobs.sort(key = lambda job: job.endTime)

        DP_endTime = [0]
        DP_profit = [0]

        for job in jobs:
            # not do the current job
            case1_profit = DP_profit[-1]

            # pick the current job
            prevIdx = self.largestSmallerIdx(DP_endTime, job.startTime + 1)
            case2_profit = DP_profit[prevIdx] + job.profit

            if case2_profit > case1_profit:
                DP_profit.append(case2_profit)
                DP_endTime.append(job.endTime)
        
        return DP_profit[-1]
    
    def largestSmallerIdx(self, arry, target):
        left, right = 0, len(arry) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if arry[mid] < target:
                left = mid
            else:
                right = mid - 1
        
        return right if arry[right] < target else left

if __name__ == "__main__":
    sol = Solution()
    print(sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    print(sol.jobScheduling([1, 2, 3, 4, 6],[3,5,10,6,9], [20,20,100,70,60]))

DP[i][j] represents

Given the first i numbers, select 0 or some of them, whether it could
sum up to j

DP[i][j] = D[i][j] || DP[i-1][j-nums[i]]
we either 
- pick the nums[i] 
- we don't pick nums[i], and DP[i-1][j-nums[i]] (the first i-1 numbers, pick 0 or some of them, whether it could sum up to j - nums[i])

the outer loop is i from 1..nums.length
the inner loop is j from 1..target

so from the above equation, we can tell the DP[i][j] only depend the last loop [i-1]

we can compress the space we need

for(int i = 1; i < nums.length; i++) {
  for (int j=target; j >= nums[i]; j--) {
    DP[j] = DP[j] || DP[j - nums[i]]
  }
}

It's important for the inner loop to start from target to nums[i]
Because
Let's we are going to compute the DP[j] when we have nums[i] coming
now in DP, it saves all the values when we have nums[0] .. nums[i-1]

when nums[i] coming, if we go from target to nums[i], then we use the lower part of DP
(which is DP[j-nums[i]]),
but if we go from nums[i] to target, when we compute j close to target, the lower part of DP may have been overwritten when go from this direction.



题目很简单 给你int n
只用加减的办法 求 1^2 + 2 ^ 2 + 3 ^ 2 + ... + n ^ 2
我的思路是 (n-1)^2 = n^2 - 2n + 1 => n^2 = (n-1)^2 + 2n -1 = (n-1)^2 + 2(n-1)+1
所以我用定义一维数组 int dp[n]

这真是一个好问题我觉得你的思路是对的

定义：dp[i] = i ^ 2
初始化dp[1] = 1
dp[i] = dp[i - 1] + (n - 1) + (n - 1) + 1 = dp[i - 1] + 2n - 1
所以最后 1^2 + 2 ^ 2 + 3 ^ 2 + ... + n ^ 2 = sum{dp[1] + dp[2] + .. + dp[n]}

这里使用到了加法和减法，你的思路非常赞。

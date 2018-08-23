- 这个题困扰我好久，网上题解包括discussion感觉都不是特别直观，现在终于完全想通了。。这里记录一下，希望能对大家有帮助。
- 这个题如果没有反复，那么显然可以用一个普通二维dp，直接求解
- 那么首先，我们想到的肯定是一个贪心的思路，先找正向一条最优的路，把路过的1变0，再重新dp一遍
这个思路是错误的，我自己验证的方法是先假设这个贪心正确，再用反证法尝试证明，在证明过程中，你就会发现一些无法cover的情况，比如一条最大权路径收益为6，两条次大收益路径相互没有重叠，收益为5，而最大路径分别和这两个次大路径重叠了2，假如其它位置都是0，那么贪心方法收益最大是9，而选两个次大路径收益是10
- 那么我们就需要重新设计dp状态，把重叠这个问题考虑进去
- 首先我们知道，正反两次走，等价于分别做两次正着走。问题就变成分别走两次找最大收益，其中第一次走过的1会变成0。
- 然后我们进一步，简化理解，可以是2个人同时正着走，且速度一样，希望两人总体的收益最大，如果它们同时走到一个格子上，那它们只能拿一次。可以简单理解一下为什么这个问题，和刚才的问题等价：设速度都是1，则第t个时刻，设第一个人走到(x1, y1)，第二个人走到(x2, y2)，那么一定有x1 + y1 = t，x2 + y2 = t，假如x1 != x2，那么这一次行程中，第一个人永远不会走到(x2, y2)，同理第二人永远不会走到(x1, y1)。因此，拿重的问题只会在它们同时走到一个格子的时候遇到，因此我们判断他们每个时刻是否会到达同一个格子就可以去重了。
- 把这个思想转换成dp的状态，则可以表示为dp(t, x1, x2)，也就是第t时刻第一个人走到(x1, t - x1)，第二个人走到(x2, t - x2)时两人的最大收益。
- 状态转移也非常简单：dp(t, x1, x2) = grid(x1, t - x1) + (x1 == x2 ? 0 : grid(x2, t - x2)) + max(dp(t-1, x1, x2), dp(t - 1, x1, x2 - 1), dp(t - 1, x1 - 1, x2), dp(t - 1, x1 - 1, x2 - 1))
最后就是t这一维我们可以通过滚动数组压掉，注意这样的话需要反向遍历更新dp

The most important part is to 
1. recognize that this is not a normal DP problem.
2. Going from 0,0 to n-1,n-1 and come back to 0,0 is equal to have two people both start from 0, 0 and reaches n-1, n-1. The whole point is to find the sum of two paths is maximum, not a single path.
3. Since they both start from 0, 0 and each time they both take only one step. So we will have this genius equation x1 + y1 = x2 + y2
4. How to construct the DP? 
x1, y1 could comes from x1-1, y1 or x1, y1 -1
x2, y2 could comes from x2-1, y2 or x2, y2 -1
So there are four cases


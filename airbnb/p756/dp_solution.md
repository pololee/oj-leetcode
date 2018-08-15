+------+------+------+
|  A   |      |      |
+--------------------+
|  D   |  E   |      |
+--------------------+
|  X   |  Y   |  Z   |
+------+------+------+

If the len(bottom) is N, the square's size is of N x N

In the question, it says
> Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
So there are 7 possible letters in total.

So we have DP[N][N][7]

DP[i][j][k]
represents at square(i,j), wether 'A' + k is allowed to there True of False

Return Value:
for x in range(7): if any DP[0][0][x] is True, then it's True

Induction:
DP[i][j][k] is True
for char 'A' + K => ch
if in allowed, ch's base is (ch_a, ch_b)
if DP[i+1][j][ch_a] is True and DP[i+1][j+1][ch_b] is True

so:
1. we build table from allowed, key is the char, value is a set of bases
2. initialize the DP and set the bottom row value
3. Then build up the DP from the second last row

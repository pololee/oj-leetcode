You are given an array of numbers [x1, x2, ... , xn] and a number M
return the number of combinations that make up the number M

无限背包问题

each item, you can pick as many as you want

                             Sum


              0     1    2     3     4    5    6     ...
           +-----+-----+----+-----+-----+----+----+
           |     |     |    |     |     |    |    |
         0 |  1  |  0  | 0  |  0  |  0  | 0  | 0  |
           |     |     |    |     |     |    |    |
           +--------------------------------------+
           |     |     |    |     |     |    |    |
         1 |  1  |     |    |     |     |    |    |
nums       |     |     |    |     |     |    |    |
           +--------------------------------------+
           |     |     |    |     |     |    |    |
         2 |  1  |     |    |     |     |    |    |
           |     |     |    |     |     |    |    |
           +--------------------------------------+
           |     |     |    |     |     |    |    |
         3 |  1  |     |    |     |     |    |    |
           |     |     |    |     |     |    |    |
           +-----+-----+----+-----+-----+----+----+
         ...

     DP[i][j] represent                       DP[0][1]
     given first i nums, the sum is j         given no nums, the sum is 1
     the # of combinations we can find        the # of combination is 0


     DP[0][0]                                 DP[0][2]
     given no nums, the sum is 0              given no nums, the sum is 1
     the number of combinations is 1          the # of combination is 0
     basically, pick nothing
                                              DP[0][3]
     DP[1][0]                                 given no nums, the sum is 1
     given 1 nums, the sum is 0               the # of combination is 0
     pick nothing,
     so the # of combinations is 1

     DP[2][0] = 1


                                             DP[2][0]
                                             given the first two items, sum is 0
                                             True because we can pick nothing

                       DP[i][j]:
                       - pick item[i], DP[i-1][j-item[i]]
                       - do not pick item[i], DP[i-1][j]

                       so



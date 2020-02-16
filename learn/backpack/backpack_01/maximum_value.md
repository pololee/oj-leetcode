[post](http://novoland.github.io/%E7%AE%97%E6%B3%95/2014/07/26/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98.html)

Given `n` objects,
the values of them are `[v0, v1, v2, ...]`
the size of them are `[c0, c1, c2, ...]`

If the `totalCapacity` of the pack is m, find the maximum value we can get.

1. state:
`DP[i][j]` represents the maximum value given the pack size is `j`, pick some objects from the `first i` objects (some of them get picked, some are not).

2. state transition function
For object `i`, size is `ci`, value is `vi`
- if it's not picked, then `DP[i][j]` would be `DP[i-1][j]` 
  (the maximum value given the pack size is `j`, pick some object from the `first i-1` objects)
- if it's picked, then `DP[i][j]` would be `DP[i-1][j-ci] + vi`
  (the value of object i + the maximum value given the pack size is `j-ci`, pick some objects from the `first i-1` objects)

So the functions is `DP[i][j] = max(DP[i-1][j], DP[i-1][j-ci] + vi)`
If `j < ci`, then `DP[i][j] = DP[i-1][j]`

3. the solution of the basic case
`DP[][0] = 0` because the pack size is 0, nothing can be put in.
`DP[0][] = 0` because no matter what size the pack is, no objects are available to pick.

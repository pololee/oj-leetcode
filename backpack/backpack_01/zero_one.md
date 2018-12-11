[post](http://novoland.github.io/%E7%AE%97%E6%B3%95/2014/07/26/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98.html)

# Maximum Value given total capacity

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


# Maximum value given total capacity, but need to **full** fill the pack

1. state:
`DP[i][j]` represents the maximum value given the pack size is `j` and the pack
is fullly filled, pick some objects from the `first i` objects
(value could be None if the pack cannot be fully filled)

2. state transition function
need to consider whether `DP[i-1][j]` and `DP[i-1][j-ci]` exists

3. the solution of the basic case
`DP[][0] = 0` pack is always full because there is no space to put and the value is 0
`DP[0][1..totalCapacity] = None` there are no ways to fully fill the pack

# Number of solution to fullfill the pack

1. state:
`DP[i][j]` represents the number of solutions to fullfile the pack given
the pack size is `j` and and pick some objects from the `first i` objects

2. state transition function
`DP[i][j] = DP[i-1][j] + DP[i][j-ci]`
If not pick object `i`, the number of solutions is `DP[i-1][j]`
If pick object `i`, the number of solutions is `DP[i][j-ci]`
When `ci > j`, `DP[i][j] = DP[i-1][j]`

3. basic case
`DP[][0] = 1` pack is empty, the number of solutions is always 1
`DP[0][1..totalCapacity] = 0` pack is not empty, but there are no objects to fill the pack. So
the number of solution is 0


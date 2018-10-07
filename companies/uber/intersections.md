You have two lists.
Each list will contain lists of length 2, which represent a range (ie. [3,5] means a range from 3 to 5, inclusive).
You need to return the intersection of all ranges between the sets. If I give you [1,5] and [0,2], the result would be [1,2].
Within each list, the ranges will always increase and never overlap (i.e. it will be [[0, 2], [5, 10] ... ] never [[0,2], [2,5] ... ])

Example:
a = [[0, 2], [5, 10], [13, 23], [24, 25b = [[1, 5], [8, 12], [15, 18], [20, 24
Expected output: [[1, 2], [5, 5], [8, 10], [15, 18], [20, 24]]
一次写过 bug free code, 一次性跑通了， 时间复杂度 O(n+m)，就这还是挂了。哎。

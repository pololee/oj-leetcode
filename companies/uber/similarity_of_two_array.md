问题是找similartiy of 2 int arrays
similartiy definition is the intersection of 2 arrays divide the union of  2 arrays.

example:
A = [3,4,1,2,7];
B = [6,1,3, 5,10];

the intersection is [1, 3]
the union is [1, 2, 3, 4, 5, 6, 7, 10]

so the similarity is 2/8

A与B的size不一定相等

一开始想了一个hash map的解法，
面试官问能否优化. Waral 博客有更多文章,
后来想到其实O(1) space 就可以解决.
但是代码没写完，题不难，但是第一次面试不会搞codepair， 与U家无缘

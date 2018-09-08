分享一个Square的店面, 是一道没见过的题(我看了十几个square的帖子, 都没有提到, 听说他们家是面试官自己想的题目....)

第一道题, 给一个数组让排序, 然而排序只可以用一个反转函数reverse(int[] array, int end), 意思就是反转数组中第0个到第end个为止的数, 比如:
[8, 7, 6. 5, 10, 1], reverse(array, 2)的话就变成[6, 7, 8, 5, 10, 1], 只能call这个反转函数直到数组中所有的数排好序为止.

第二道题, 第一题的follow up, 现在给的是布尔数组, 还是反转函数reverse(array, end), 只是除了反转以外, 需要反转的数都要被取反, 比如:
[true, false, false, false, true, true], reverse(array, 2)的话, 就变成[true, true, false, false, true, true], 需要最后把这个数组变成[true, true, true, true, true,  true]

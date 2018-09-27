题目是假如对于Uber eat，有一大堆记录，每条记录有id，订了什么食物，是几点订的。其中几点定的只有0-23这24个可能。

比如：
(0, apple, 0)
(1, apple, 0)
(2, orange, 1)
(3, orange, 0)

让找出每个小时的top K selling food。

难度不大，我是对0-23点每个小时建一个hash map，里面key是food，value是被订的次数，然后遍历这些记录更新这些map，最后对从每个小时的map中找出top k的food。
. 1point3acres
在每个小时的map里找top K的food的时候是用min heap的方法做的

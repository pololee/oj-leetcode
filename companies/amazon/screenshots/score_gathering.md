Score gathering 
We have a system that records scores. We care about how many times we see the same score, and we want to maintain a rough ordering. We also want to send this information over the wire so that it can be collated with other results. As such we have decided to represent the stream of scores, and the count of how many times we see the same score, as an unbalanced binary search tree. 
Your job is to write a method that will take a stream of integer scores, and put them into a tree while counting the number of times each score is seen. The first score from the given list should occupy the root node. Then you need to traverse the tree breadth-first to generate a string representation of the tree. Scores are to be inserted into the tree in the order that they are given. 
For example, if you were given the stream of scores: 4, 2, 5, 5, 6, 1, 4 That would result in the tree with the following structure where each node is represented as <score>:<count>. 4:2 
/ \ 
2:1 5:2 

6:1 
When serialized this tree is represented by the string: 4:2,2:1, 5:2, 1:1„ , 6:1 Each <score>:<count> entry is delimited with a comma. Empty children with a sibling do not output anything, but retain the comma delimiter. 

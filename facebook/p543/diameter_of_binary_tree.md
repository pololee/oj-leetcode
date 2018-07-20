Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

### Notes from Polo:
Looks simple but you have to be careful.
Some jerk always post confusing solution online. What's good is that they are posting solution.
What's bad is that it makes you very upset.

So let's think a different problem first. The maximum height (or depth) of a binray tree
It's defined as the maximum number of nodes along a path from the root node to the leaf node.
Or the number of nodes along the from from the root node to the deepest leaf node.

MaxDepth(root) = max(MaxDepth(root.left), MaxDepth(root.right)) + 1

Given a node, if I know its max depth of its left child maxDepthLeft and right child max, then 
the diameter path will be
the path of left max depth, across the root, and connect the path of right max depth

the diameter length will be
the length of the left max depth path + 1 + 1 + the length of the right max depth path
Note the definition of depth is number of nodes
So the length of the left max depth path = left max depth - 1

So the diameter length will be
left max depth - 1 + 1 + 1 + right max depth -1
left max depth + right max depth

See the difference: diameter is left max depth + right max depth
whereas the depth of root = max(MaxDepth(root.left), MaxDepth(root.right)) + 1

So in this solution, the whole structure is to compute the max depth. The diameter computation is taking
the train of the depth computation.

Solution:
O(n^2)
- what pathSum does? 
  Return the number of possible paths that sum up to target.
  Just believe it will return the right thing.
  So first, we get pathSum(root.left, target) and pathSum(root.right, target)
  Now we have the number of possible paths that sum up to target from both left subtree and right subtree.
  Next, we'll need to find the number of paths that sum up to target, including the root node.

- What contain_path does?
  Return the number of possible paths that sum up to target, including the root node, i.e.
  start from the root node.
  we can divide the problem again
  Find the number of possible paths that sum up to target - root.val, from the left child
  Find the number of possible paths that sum up to target - root.val, from the right child
  If the root itself == sum, it can be a single path sum up to target
  Now the return value will be the total above

BetterSolution:
O(n)
- Use a list to save all the path sums we find
- From bottom up
  

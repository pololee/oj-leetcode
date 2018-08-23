- The squirrel can only take at most one nut at one time.
- So after the squirrel takes the first and put it under the tree, it needs to go from the tree and collect all the others nuts one by one. For the rest of the nuts, the distance is 2 * (distance from the tree to the nut)
- Based the above analysis, we can tell once the first nut is decided, then the total distance is decided.

Distance 
- the first nut: distance(tree, nut) + distance(nut, squirrel)
- the other nut: distance(tree, nut) + distance(nut, tree)

i.e.
- the first nut: distance(tree, nut) + distance(tree, nut) + distance(nut, squirrel) - distance(tree, nut)
- the other nut: distance(tree, nut) + distance(tree, nut)

All we need to find the minimum -> distance(nut, squirrel) - distance(tree, nut)

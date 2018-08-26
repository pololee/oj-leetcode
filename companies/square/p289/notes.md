- The board needs to be updated at the same time. We cannot just update some cells first and then use their updated values to update other cells

But in our code, we still have to go through each cell one by one.
We can use numbers to represent state change, not the state

0: from dead to dead
1: from live to live
2: from live to dead
3: from dead to live

After we fill in the transition value of each cell,
we could use % 2 on each cell's value, which gives
use the final board.

## Rules: 8 neighbors
  < 2 live neighbors => live -> dead     2
  2 or 3 live neighbors => live -> live  1
  > 3 live neighbors => live -> dead     2
  == 3 live neighbors => dead -> live    3

- use two stacks, one for operators, one for numbers
  - why stack? because the operation you are seeing right now may depends on the future operations. e.g. 2 - 1 * 3, when you look at -, you shouldn't compute it now, because it depends on future *

- This part is very important

Compare the current operator and the previous operator

case 1:
(5 +
previous ( and current +, no way to perform ops

case 2:
5 + 6 * 3
5 - 6 * 3
5 + 6 / 3
5 - 6 / 3

previous +, -  current  *, /
should not perform ops, because we should calculate 6 * or / 3 first

Think about stack, if perform the operation backforward, we want to make sure things in the stack will be calculated correctly as we go in backforward direction.

case 3:

5 * 3 + 6
5 * 3 - 6
5 / 3 + 6
5 / 3 - 6
5 + 3 - 6
5 - 3 - 6
5 - 3 + 6
5 + 3 + 6

we need to perform ops for the previous ops
  
```python
    def should_perform_ops(self, previous, current):
        if previous == '(':
            return False

        if (current == '*' or current == '/') and (previous == '+' or previous == '-'):
            return False

        return True
```

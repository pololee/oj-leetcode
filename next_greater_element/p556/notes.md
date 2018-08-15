1. The question is asking the smallest number that is greater than the given number
2. Here are a few examples:
  - 54321 -> -1
  - 354321 -> 412335
    - From the right end to the left start, find the bottom of the first valley. e.g. it's 3
    - From the right end to the left start, find the first number that is greater than the above valley bottom.
      e.g it's 4.
    - swap the above two found position
    - from the right of the above valley bottom position, reverse the right part.
3. Be careful about overflow case

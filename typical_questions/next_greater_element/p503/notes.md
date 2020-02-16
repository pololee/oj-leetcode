1. when the question mentions `"circular array"`, you will most likely need to loop the array
from the beginning to 2 * length(array). Just think it as double the array and connect them together

2. In "next greater element i", we push the value to stack, because the question says there are no duplicates.
But in this question, we need to push the `"index"` to stack. We need to deal with duplicate elements.

/**
 * Let us consider an example where each element is a person's birthday.
 * Your birthday, say some day in March, is the new element xx.
 * Suppose that each month has 3030 days and you want to know
 * if anyone has a birthday within t = 30t=30 days of yours.
 * Immediately, we can rule out all other months except February, March, April.
 *
 * The reason we know this is because each birthday
 * belongs to a bucket we called month! And the range covered by the buckets
 * are the same as distance tt which simplifies things a lot.
 * Any two elements that are not in the same or adjacent buckets
 * must have a distance greater than t
 * .
 * We apply the above bucketing principle and design buckets covering
 * the ranges of ..., [0,t], [t+1, 2t+1], ......,[0,t],[t+1,2t+1],....
 * We keep the window using this buckets. Then, each time,
 * all we need to check is the bucket that xx belongs to and its two adjacent buckets.
 *
 * Thus, we have a constant time algorithm for searching almost duplicate in the window.
 * One thing worth mentioning is the difference from bucket sort –
 * Each of our buckets contains at most one element at any time,
 * because two elements in a bucket means "almost duplicate"
 * and we can return early from the function.
 * Therefore, a HashMap with an element associated with
 * a bucket label is enough for our purpose.
 */

package airbnb.p220;

import java.util.Map;
import java.util.HashMap;

public class BucketSolution {
  /**
   * when number is negative, and bucket size is 5
   * say number is -3, -3/5 = 0, but we want it to be -1
   * say number is -6, -6/5 = -1, but we want it to be -2
   * so we have number/bucketSize - 1
   *
   * however when number is -5, it will be -2
   * but we want it to be -1,
   * so we have (number + 1)/bucketSize - 1
   *
   */
  private long getBucketLabel(long number, long bucketSize) {
    if (number < 0) {
      return (number + 1) / bucketSize - 1;
    } else {
      return number / bucketSize;
    }
  }

  /**
   * [containsNearbyAlmostDuplicate description]
   * @param  nums [description]
   * @param  k    index difference at most k
   * @param  t    value difference at most t
   * @return      [description]
   */
  public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if(t < 0 || k < 0) return false;

    Map<Long, Long> map = new HashMap<>();
    long bucketSize = (long)t + 1;

    for(int i = 0; i < nums.length; i++) {
      long number = (long)nums[i];
      long bucketLabel = getBucketLabel(number, bucketSize);

      if(map.containsKey(bucketLabel))
        return true;
      // < bucketSize because bucketSize = t + 1, which means it <= t
      if(map.containsKey(bucketLabel - 1) && Math.abs(number - map.get(bucketLabel - 1)) < bucketSize)
        return true;
      // < bucketSize because bucketSize = t + 1, which means it <= t
      if(map.containsKey(bucketLabel + 1) && Math.abs(number - map.get(bucketLabel + 1)) < bucketSize)
        return true;

      map.put(bucketLabel, number);
      // make sure index difference at most k
      if(i >= k)
        map.remove(getBucketLabel(nums[i-k], bucketSize));
    }

    return false;
  }
}
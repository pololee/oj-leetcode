package airbnb.p220;

import java.util.Map;
import java.util.HashMap;

public class BucketSolutionII {
  private long getBucketLabel(long number, long bucketSize) {
    return (number - Integer.MIN_VALUE) / bucketSize;
  }

  /**
   * [containsNearbyAlmostDuplicate description]
   * @param  nums [description]
   * @param  k    index difference at most k
   * @param  t    value difference at most t
   * @return      [description]
   */
  public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if(k < 0 || t < 0) return false;

    long bucketSize = (long)t + 1;
    Map<Long, Long> map = new HashMap<>();

    for(int i = 0; i < nums.length; i++) {
      long number = (long)nums[i];
      long bucketLabel = getBucketLabel(number, bucketSize);

      if(map.containsKey(bucketLabel))
        return true;
      if(map.containsKey(bucketLabel - 1) && Math.abs(number - map.get(bucketLabel - 1)) < bucketSize)
        return true;
      if(map.containsKey(bucketLabel + 1) && Math.abs(number - map.get(bucketLabel + 1)) < bucketSize)
        return true;

      map.put(bucketLabel, number);
      if(i >= k)
        map.remove(getBucketLabel((long)nums[i-k], bucketSize));
    }

    return false;
  }
}
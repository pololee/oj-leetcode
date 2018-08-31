import java.util.Arrays;

public class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        if(nums == null || nums.length == 0) 
            return false;
        
        if(k > nums.length) 
            return false;
        
        int total = 0;
        for(int x : nums) {
            total += x;
        }
        
        if (total % k != 0)
            return false;
        
        Arrays.sort(nums);
        int target = total / k;
        int[] bucket = new int[k];
        return dfsUtil(bucket, target, nums, nums.length - 1);
    }
    
    private boolean dfsUtil(int[] bucket, int target,  int[] nums, int idx) {
        if (idx == -1) {
            for(int x : bucket) {
                if(x != target) {
                    return false;
                }
            }    
            return true;
        }
        
        int num = nums[idx];
        for(int i = 0; i < bucket.length; i++) {
            if (bucket[i] + num > target) 
                continue;
            bucket[i] += num;
            
            if (dfsUtil(bucket, target, nums, idx - 1)) {
                return true;
            }

            bucket[i] -= num;
        }
        
        return false;
    }
}

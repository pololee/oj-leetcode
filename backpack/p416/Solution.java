class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length < 2)
            return false;
        
        int total = 0;
        for(int x : nums)
            total += x;
        
        if(total % 2 != 0)
            return false;
        
        int target = total / 2;
        int[][] DP = new int[nums.length + 1][target + 1];
        DP[0][0] = 1;
        
        for(int i = 1; i < nums.length + 1; i++)
            DP[i][0] = 1;
        
        for(int i = 1; i < nums.length + 1; i++) {
            int num = nums[i-1];
            for (int j = 1; j < target + 1; j++) {
                if(DP[i-1][j] == 1 || (j >= num && DP[i-1][j-num] == 1)) {
                    DP[i][j] = 1;
                }
            }
        }
        
        return DP[nums.length][target] == 1;
    }
}

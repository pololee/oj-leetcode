# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  h = {}
  nums.each_index do |idx|
    return [h[target - nums[idx]] + 1, idx + 1] unless h[target - nums[idx]].nil?
    h[nums[idx]] = idx
  end
end

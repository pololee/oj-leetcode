# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}

def two_sum_sorted(nums, target)
  max = nums.length - 1
  for i in 0..max
    j = binary_search(nums, target - nums[i], i + 1)
    return [i, j] if j != -1
  end

  raise 'Cannot find the pair'
end

def two_sum_sorted_best(nums, target)
  min = 0
  max = nums.length - 1
  while min < max
    sum = nums[min] + nums[max]
    if sum > target
      max -= 1
    elsif sum < target
      min += 1
    else
      return [min, max]
    end
  end

  raise 'Cannot find the pair'
end

def binary_search(nums, key, start)
  l = start
  r = nums.length - 1
  while l < r
    m = (l + r)/2
    if nums[m] < key
      l = m + 1
    else
      r = m
    end
  end

  l == r && nums[l] == key ? l : -1
end

nums = [2, 7, 11, 15]
target = 9
puts two_sum_sorted(nums, target)
puts two_sum_sorted_best(nums, target)
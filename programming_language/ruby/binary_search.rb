def binary_search(array, target)
  min = 0
  max = array.length - 1;

  while(min <= max)
    guess = (min + max)/2
    if array[guess] == target
      return guess
    elsif array[guess] < target
      min = guess + 1
    else
      max = guess - 1
    end
  end

  return -1
end

def deferred_detection_binary_search(array, target)
  min = 0
  max = array.length - 1;

  while min < max
    m = (min + max) / 2
    if array[m] < target
      min = m + 1
    else
      max = m
    end
  end

  puts "min after loop #{min}"
  puts "max after loop #{max}"

  min == max && array[min] == target ? min : -1
end

array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# puts binary_search(array, 73)
# puts deferred_detection_binary_search(array, 73)

test2 = [1, 3, 5]

# deferred_detection_binary_search
# After the loop, min must equal to max.
# 1: nums[min] == target, then min is the index we look for
# 2: target > nums[min] && target < nums[min], then min is the position where the target should be
# 3: target < nums[min]
# 4: target > nums[min]

puts "#{test2}, look for 6"
puts deferred_detection_binary_search(test2, 6)
puts "#{test2}, look for 4"
puts deferred_detection_binary_search(test2, 4)
puts "#{test2}, look for 0"
puts deferred_detection_binary_search(test2, 0)
puts "#{test2}, look for 2"
puts deferred_detection_binary_search(test2, 2)


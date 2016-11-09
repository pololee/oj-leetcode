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

  min == max && array[min] == target ? min : -1
end

array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
puts binary_search(array, 73)
puts deferred_detection_binary_search(array, 73)

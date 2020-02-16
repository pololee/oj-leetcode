def find_two_sum_ii(sorted_arry, sum)
  low = 0
  high = sorted_arry.length - 1

  while low < high
    if sorted_arry[low] + sorted_arry[high] > sum
      high -= 1
    elsif sorted_arry[low] + sorted_arry[high] < sum
      low += 1
    else
      return [low + 1, high + 1]
    end
  end
end

puts find_two_sum_ii([1, 2, 3, 5], 5)

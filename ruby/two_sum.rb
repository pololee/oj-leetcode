def find_two_sum(arry, sum)
  h = {}
  result = nil

  arry.each_with_index do |item, index|
    if h[sum - item]
      result = [h[sum - item] + 1, index + 1]
    else
      h[item] = index
    end
  end

  result
end

test = [5, 2, 1, 3]
sum = 5
puts find_two_sum(test, sum)

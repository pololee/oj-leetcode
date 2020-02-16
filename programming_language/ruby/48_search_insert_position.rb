def search_insert_position(arry, target)
  l = 0
  r = arry.size - 1

  while l < r
    m = (l + r) / 2
    if arry[m] < target
      l = m + 1
    else
      r = m
    end
  end

  arry[l] > target ? l + 1 : l
end

# When the while loop ends, l must be equal to r and it is a valid index.
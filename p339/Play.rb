def depth_sum(nested_list)
  nested_list.reduce(0) do |memo, nested|
    memo + depth_sum_util(nested, 1)
  end
end

def depth_sum_util(nested, level)
  if nested.is_a?(Integer)
    nested * level
  else
    nested.reduce(0) do |memo, nest|
      memo + depth_sum_util(nest, level + 1)
    end
  end
end

p depth_sum([[1, 1], 2, [1, 1]])
p depth_sum([1, [4, [6]]])

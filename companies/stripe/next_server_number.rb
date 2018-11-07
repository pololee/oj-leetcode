# frozen_string_literal: true

require 'set'

class NextServerNumber
  def next_number(nums: [])
    return 1 if nums.empty?

    nums_set = Set.new(nums)
    max_num = nums_set.max

    (1..max_num).to_a.each do |num|
      return num unless nums_set.member?(num)
    end

    max_num + 1
  end
end
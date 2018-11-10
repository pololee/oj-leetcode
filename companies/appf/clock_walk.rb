# Given two clock number a, b
# return the direction clock-wise or counter-clock-wise
# which give the fastest way to go from a to b

require "minitest/autorun"

class Solution
  SIZE = 12

  def shortest_dist(start, fin)
    clock_wise = clockwise_dist(start, fin)
    counter_clockwise = counter_clockwise_dist(start, fin)

    if clock_wise < counter_clockwise
      ['clockwise', clock_wise]
    else
      ['counter clockwise', counter_clockwise]
    end
  end

  private

  def clockwise_dist(start, fin)
    (SIZE + fin - start) % SIZE
  end

  def counter_clockwise_dist(start, fin)
    SIZE - clockwise_dist(start, fin)
  end
end

class SolutionTest < Minitest::Test
  def test_shortest_dist
    sol = Solution.new
    assert_equal ['clockwise', 0], sol.shortest_dist(1, 1)
    assert_equal ['clockwise', 5], sol.shortest_dist(2, 7)
    assert_equal ['counter clockwise', 5], sol.shortest_dist(7, 2)
    assert_equal ['counter clockwise', 4], sol.shortest_dist(2, 10)
    assert_equal ['clockwise', 4], sol.shortest_dist(10, 2)
    assert_equal ['clockwise', 3], sol.shortest_dist(12, 3)
  end
end

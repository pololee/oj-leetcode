require 'minitest/autorun'
require_relative './record_finder'

class RecordFinderTest < MiniTest::Test
  def setup
    @finder = RecordFinder.new
  end

  def test_min_by_key
    example1 = [{ 'a' => 1, 'b' => 2 }, { 'a' => 2 }]
    example2 = [example1[1], example1[0]]
    example3 = [{}]
    example4 = [{ 'a' => -1 }, { 'b' => -1 }]

    assert_equal(example1[0], @finder.min_by_key('a', example1))
    assert_equal(example2[1], @finder.min_by_key('a', example2))
    assert_equal(example1[1], @finder.min_by_key('b', example1))
    assert_equal(example3[0], @finder.min_by_key('a', example3))
    assert_equal(example4[1], @finder.min_by_key('b', example4))
  end

  def test_first_by_key
    example1 = [{ 'a' => 1 }]
    example2 = [{ 'b' => 1 }, { 'b' => -2 }, { 'a' => 10 }]
    example3 = [{}, { 'a' => 10, 'b' => -10 }, {}, { 'a' => 3, 'c' => 3 }]

    assert_equal(example1[0], @finder.first_by_key('a', 'asc', example1))
    assert_includes([example2[0], example2[1]], @finder.first_by_key('a', 'asc', example2))
    assert_equal(example2[2], @finder.first_by_key('a', 'desc', example2))
    assert_equal(example2[1], @finder.first_by_key('b', 'asc', example2))
    assert_equal(example2[0], @finder.first_by_key('b', 'desc', example2))
    assert_equal(example3[1], @finder.first_by_key('a', 'desc', example3))
  end

  def test_last_by_sort_order
    assert_equal(
      { 'a' => 1, 'b' => 1 },
      @finder.last_by_sort_order(
        [['a', 'asc'], ['b', 'desc']],
        [{ 'a' => 1, 'b' => 2 }, { 'a' => 1, 'b' => 1 }]
      )
    )
  end

  def test_first_by_sort_order
    assert_equal(
      { 'a' => 6 },
      @finder.first_by_sort_order([['a', 'desc']], [{ 'a' => 5 }, { 'a' => 6 }])
    )

    assert_equal(
      { 'a' => -4, 'b' => 10 },
      @finder.first_by_sort_order(
        [['b', 'asc'], ['a', 'desc']],
        [{ 'a' => -5, 'b' => 10 }, { 'a' => -4, 'b' => 10 }]
      )
    )

    assert_equal(
      { 'a' => -5, 'b' => 10 },
      @finder.first_by_sort_order(
        [['a', 'asc'], ['b', 'asc']],
        [{ 'a' => -5, 'b' => 10 }, { 'a' => -4, 'b' => 10 }]
      )
    )
  end

  # def test_first_k_by_sort_order
  #   assert_equal(
  #     [{ 'b' => 1 }, { 'a' => 1, 'b' => 2 }],
  #     @finder.first_k_by_sort_order(
  #       2,
  #       [['a', 'asc'], ['b', 'desc']],
  #       [{ 'a' => 1, 'b' => 2 }, { 'a' => 1 }, { 'b' => 1 }]
  #     )
  #   )
  # end
end

class RecordComparatorTest < MiniTest::Test
  def test_compare
    cmp = RecordComparator.new('a', 'asc')
    assert_equal(-1, cmp.compare({ 'a' => 1 }, 'a' => 2))
    assert_equal(1, cmp.compare({ 'a' => 2 }, 'a' => 1))
    assert_equal(0, cmp.compare({ 'a' => 1 }, 'a' => 1))
  end
end

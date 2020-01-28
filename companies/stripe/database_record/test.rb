require 'minitest/autorun'

class ToyDataBase
  DIRECTIONS = {
    asc: 'asc',
    desc: 'desc'
  }.freeze

  def min_by_key(key, records)
    first_by_key(key, DIRECTIONS[:asc], records)
  end

  def first_by_key(key, direction, records)
    return {} if records.empty?

    raise ArgumentError.new("unknown direction #{direction}") unless DIRECTIONS.values.include?(direction)

    ans = records[0]
    cmp = RecordComparator.new(key, direction)
    records[1..-1].each do |rec|
      ans = rec if cmp.compare(rec, ans).negative?
    end

    ans
  end

  def last_by_sort_order(sort_order, records)
    return {} if records.empty?

    ans = records[0]
    cmd = SortOrderCmd.new('last', sort_order)
    records[1..-1].each do |rec|
      ans = rec if cmd.should_replace?(rec, ans)
    end

    ans
  end

  def first_by_sort_order(sort_order, records)
    return {} if records.empty?

    ans = records[0]
    cmd = SortOrderCmd.new('first', sort_order)
    records[1..-1].each do |rec|
      ans = rec if cmd.should_replace?(rec, ans)
    end

    ans
  end
end

class SortOrderCmd
  def initialize(order, sort_order)
    @order = order
    @cmps = record_comparators(sort_order)
  end

  def should_replace?(candidate, original)
    @cmps.each do |cmp|
      next if cmp.compare(candidate, original).zero?

      return @order == 'first' if cmp.compare(candidate, original).negative?
      return @order == 'last' if cmp.compare(candidate, original).positive?
    end

    false
  end

  private

  def record_comparators(sort_order)
    sort_order.map do |order|
      raise ArgumentError.new("invalid order #{order}") unless ToyDataBase::DIRECTIONS.values.include?(order[1])

      RecordComparator.new(order[0], order[1])
    end
  end
end

class RecordComparator
  attr_reader :key, :direction

  def initialize(key, direction)
    @key = key
    @direction = direction
  end

  def compare(left, right)
    left_value = left.fetch(key, 0)
    right_value = right.fetch(key, 0)

    if left_value == right_value
      0
    elsif left_value < right_value
      ToyDataBase::DIRECTIONS[:asc] == direction ? -1 : 1
    else
      ToyDataBase::DIRECTIONS[:asc] == direction ? 1 : -1
    end
  end
end

class ToyDataBaseTest < Minitest::Test
  def setup
    @finder = ToyDataBase.new
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
end

class RecordComparatorTest < Minitest::Test
  def test_compare
    cmp = RecordComparator.new('a', 'asc')
    assert_equal(-1, cmp.compare({ 'a' => 1 }, 'a' => 2))
    assert_equal(1, cmp.compare({ 'a' => 2 }, 'a' => 1))
    assert_equal(0, cmp.compare({ 'a' => 1 }, 'a' => 1))
  end
end

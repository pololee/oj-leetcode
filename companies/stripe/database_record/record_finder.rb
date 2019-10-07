class RecordFinder
  DIRECTIONS = {
    asc: 'asc',
    desc: 'desc'
  }.freeze

  def min_by_key(key, records)
    first_by_key(key, DIRECTIONS[:asc], records)
  end

  def first_by_key(key, direction, records)
    first_by_sort_order([[key, direction]], records)
  end

  def last_by_sort_order(sort_order, records)
    return {} if records.empty?

    cmps = sort_order.map do |order|
      raise ArgumentError.new("unknown order #{order}") unless DIRECTIONS.values.include?(order[1])

      RecordComparator.new(order[0], order[1])
    end

    ans = records[0]
    records[1..-1].each do |rec|
      cmps.each do |cmp|
        next if cmp.compare(rec, ans).zero?
        break if cmp.compare(rec, ans).negative?

        ans = rec
        break
      end
    end

    ans
  end

  def first_by_sort_order(sort_order, records)
    return {} if records.empty?

    cmps = sort_order.map do |order|
      raise ArgumentError.new("unknown order #{order}") unless DIRECTIONS.values.include?(order[1])

      RecordComparator.new(order[0], order[1])
    end

    ans = records[0]
    records[1..-1].each do |rec|
      cmps.each do |cmp|
        next if cmp.compare(rec, ans).zero?
        break if cmp.compare(rec, ans).positive?

        ans = rec
        break
      end
    end

    ans
  end

  # def first_k_by_sort_order(k, sort_order, records); end
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
      RecordFinder::DIRECTIONS[:asc] == direction ? -1 : 1
    else
      RecordFinder::DIRECTIONS[:asc] == direction ? 1 : -1
    end
  end
end

class SortOrder
  ORDERS = {
    first: 'first',
    last: 'last'
  }.freeze

  attr_reader :order, :comparators

  def initialize(order, comparators)
    @order = order
    @comparators = comparators
  end

  def compare(left, right)
    comparators.each do |cmp|
      next if cmp.compare(left, right).zero?
      return ORDERS[:first] == order ? -1 : 1 if cmp.compare(left, right).negative?

      return ORDERS[:first] == order ? 1 : -1
    end
    0
  end
end

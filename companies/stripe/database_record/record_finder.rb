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

    ans = records[0]
    sort_order_cmd = SortOrderCmd.new('last', sort_order)
    records[1..-1].each do |rec|
      ans = rec if sort_order_cmd.should_replace?(rec, ans)
    end

    ans
  end

  def first_by_sort_order(sort_order, records)
    return {} if records.empty?

    ans = records[0]
    sort_order_cmd = SortOrderCmd.new('first', sort_order)
    records[1..-1].each do |rec|
      ans = rec if sort_order_cmd.should_replace?(rec, ans)
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

class SortOrderCmd
  attr_reader :order, :cmps

  def initialize(order, sort_order)
    @order = order
    @cmps = record_comparators(sort_order)
  end

  def should_replace?(candidate, target)
    cmps.each do |cmp|
      next if cmp.compare(candidate, target).zero?

      return order == 'first' if cmp.compare(candidate, target).negative?
      return order == 'last' if cmp.compare(candidate, target).positive?
    end

    false
  end

  private

  def record_comparators(sort_order)
    sort_order.map do |order|
      raise ArgumentError.new("invalid order #{order}") unless RecordFinder::DIRECTIONS.values.include?(order[1])

      RecordComparator.new(order[0], order[1])
    end
  end
end

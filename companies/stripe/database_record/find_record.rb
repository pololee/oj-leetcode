# frozen_string_literal: true

class FindRecord
  DIRECTIONS =
    {
      asc: 'asc',
      desc: 'desc'
    }.freeze

  def min_by_key(key:, records:)
    first_by_key(key: key, direction: DIRECTIONS[:asc], records: records)
  end

  def first_by_key(key:, direction:, records: [])
    first_sort_by_key(sort_orders: [[key, direction]], records: records)
  end

  def first_sort_by_key(sort_orders: [], records: [])
    return {} if sort_orders.empty? || records.empty?

    comparators = sort_orders.map do |order|
      raise Exception.new("invalid direction: #{order[1]}") unless DIRECTIONS.values.include?(order[1])

      RecordComparator.new(key: order[0], direction: order[1])
    end

    answer = records[0]
    records[1..].each do |record|
      comparators.each do |comparator|
        if comparator.compare(record, answer).negative?
          answer = record
          break
        end
      end
    end

    answer
  end
end

class RecordComparator
  attr_reader :key, :direction

  def initialize(key:, direction:)
    @key = key
    @direction = direction
  end

  def compare(a, b)
    a_value = a.fetch(key, 0)
    b_value = b.fetch(key, 0)

    if a_value == b_value
      0
    elsif a_value < b_value
      direction == FindRecord::DIRECTIONS[:asc] ? -1 : 1
    else
      direction == FindRecord::DIRECTIONS[:asc] ? 1 : -1
    end
  end
end

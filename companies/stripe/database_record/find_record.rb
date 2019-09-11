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
    return {} if records.empty?

    raise Exception.new("invalid direction: #{direction}") unless DIRECTIONS.values.include?(direction)

    answer = records[0]
    comparator = RecordComparator.new(key: key, direction: direction)
    records[1..].each do |record|
      answer = record if comparator.compare(record, answer).negative?
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

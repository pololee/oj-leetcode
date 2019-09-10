# frozen_string_literal: true

class FindRecord
  DIRECTIONS =
    {
      asc: 'asc',
      desc: 'desc'
    }.freeze

  def min_by_key(key:, records:)
    return {} if records.nil? || records.empty?

    answer = records[0]
    records[1..].each do |record|
      answer = record if record.fetch(key, 0) < answer.fetch(key, 0)
    end

    answer
  end

  def first_by_key(key:, direction:, records: [])
    return {} if records.empty?

    if direction != DIRECTIONS[:asc] && direction != DIRECTIONS[:desc]
      raise Exception.new("invalid direction: #{direction}")
    end

    answer = records[0]
    records[1..].each do |record|
      if direction == DIRECTIONS[:asc]
        answer = record if record.fetch(key, 0) < answer.fetch(key, 0)
      elsif direction == DIRECTIONS[:desc]
        answer = record if record.fetch(key, 0) > answer.fetch(key, 0)
      end
    end

    answer
  end
end

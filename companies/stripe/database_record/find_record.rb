# frozen_string_literal: true

class FindRecord
  def min_by_key(key:, records:)
    return {} if records.nil? || records.empty?

    answer = records[0]
    records[1..].each do |record|
      answer = record if record.fetch(key, 0) < answer.fetch(key, 0)
    end

    answer
  end
end

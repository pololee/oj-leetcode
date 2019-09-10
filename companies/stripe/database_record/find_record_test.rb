# frozen_string_literal: true

require '../test_helper'
require './find_record'

class FindRecordTest < Minitest::Test
  def test_min_by_key
    fr = FindRecord.new

    assert_equal({ a: 1, b: 2 }, fr.min_by_key(key: :a, records: [{ a: 1, b: 2 }, { a: 2 }]))
    assert_equal({ a: 1, b: 2 }, fr.min_by_key(key: :a, records: [{ a: 2 }, { a: 1, b: 2 }]))
    assert_equal({ a: 2 }, fr.min_by_key(key: :b, records: [{ a: 1, b: 2 }, { a: 2 }]))
    assert_equal({}, fr.min_by_key(key: :a, records: [{}]))
    assert_equal({ b: -1 }, fr.min_by_key(key: :b, records: [{ a: -1 }, { b: -1 }]))
  end
end

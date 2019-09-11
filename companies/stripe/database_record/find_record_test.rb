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

  def test_first_by_key__empty
    fr = FindRecord.new

    assert_empty fr.first_by_key(key: :a, direction: 'asc')
  end

  def test_first_by_key__invalid_direction
    fr = FindRecord.new

    assert_raises Exception do
      fr.first_by_key(key: :a, direction: 'invalid', records: [{ a: 1 }])
    end
  end

  def test_first_by_key
    fr = FindRecord.new

    assert_equal(
      { 'a': 1 },
      fr.first_by_key(
        key: 'a',
        direction: FindRecord::DIRECTIONS[:asc],
        records: [{ "a": 1 }]
      )
    )
    assert_includes(
      [{ b: 1 }, { b: -2 }],
      fr.first_by_key(
        key: :a,
        direction: FindRecord::DIRECTIONS[:asc],
        records: [{ b: 1 }, { b: -2 }, { a: 10 }]
      )
    )
    assert_equal(
      { a: 10 },
      fr.first_by_key(
        key: :a,
        direction: FindRecord::DIRECTIONS[:desc],
        records: [{ b: 1 }, { b: -2 }, { a: 10 }]
      )
    )
    assert_equal(
      { b: -2 },
      fr.first_by_key(
        key: :b,
        direction: FindRecord::DIRECTIONS[:asc],
        records: [{ b: 1 }, { b: -2 }, { a: 10 }]
      )
    )
    assert_equal(
      { b: 1 },
      fr.first_by_key(
        key: :b,
        direction: FindRecord::DIRECTIONS[:desc],
        records: [{ b: 1 }, { b: -2 }, { a: 10 }]
      )
    )
    assert_equal(
      { a: 10, b: -10 },
      fr.first_by_key(
        key: :a,
        direction: FindRecord::DIRECTIONS[:desc],
        records: [{}, { a: 10, b: -10 }, {}, { a: 3, c: 3 }]
      )
    )
  end
end

class RecordComparatorTest < Minitest::Test
  def test_compare__asc
    comparator = RecordComparator.new(key: :a, direction: FindRecord::DIRECTIONS[:asc])
    assert_equal(-1, comparator.compare({ a: 1 }, a: 2))
    assert_equal 1, comparator.compare({ a: 2 }, a: 1)
    assert_equal 0, comparator.compare({ a: 1 }, a: 1)
    assert_equal 1, comparator.compare({ a: 1 }, b: 1)
  end

  def test_compare__desc
    comparator = RecordComparator.new(key: :a, direction: FindRecord::DIRECTIONS[:desc])

    assert_equal(1, comparator.compare({ a: 1 }, a: 2))
    assert_equal(-1, comparator.compare({ a: 2 }, a: 1))
    assert_equal(0, comparator.compare({ a: 1 }, a: 1))
    assert_equal(-1, comparator.compare({ a: 1 }, b: 1))
  end
end

require 'minitest/autorun'

class RecordFinder
  def min_by_column(records, key)
    return {} if records.empty?

    ans = records[0]
    records[1..-1].each do |rec|
      ans = rec if rec.fetch(key, 0) < ans.fetch(key, 0)
    end

    ans
  end

  def min_by_order(records, columns)
    return {} if records.empty?

    ans = records[0]
    records[1..-1].each do |rec|
      columns.each do |col|
        rec_value = rec.fetch(col, 0)
        ans_value = ans.fetch(col, 0)

        next if rec_value == ans_value
        break if rec_value > ans_value

        ans = rec
        break
      end
    end

    ans
  end
end

class RecordFinderTest < MiniTest::Test
  def setup
    @finder = RecordFinder.new
  end

  def test_min_by_column
    table1 = [
      { 'a' => 1 },
      { 'a' => 2 },
      { 'a' => 3 }
    ]
    assert_equal(
      { 'a' => 1 },
      @finder.min_by_column(table1, 'a')
    )
  end

  def test_min_by_order
    table2 = [
      { 'x' => 1, 'y' => 3 },
      { 'x' => 1, 'y' => 0 }
    ]
    assert_equal(
      table2[1],
      @finder.min_by_order(table2, ['x', 'y'])
    )

    table3 = [
      { 'x' => 3, 'y' => -1, 'z' => 0 },
      { 'x' => 1, 'y' => 10, 'z' => 1 },
      { 'x' => 1, 'y' => 10, 'z' => 0 }
    ]
    assert_equal(
      table3[2],
      @finder.min_by_order(table3, ['x', 'y', 'z'])
    )
  end
end

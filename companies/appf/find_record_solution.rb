def min_by_key(key, records)
  first_by_key(key, "asc", records)
end

def first_by_key(key, direction, records)
  return {} if records.empty?

  ans = records[0]
  cmp = Comparator.new(key, direction)

  records.each do |record|
    ans = record if cmp.compare(record, ans) < 0
  end

  ans
end

class Comparator
  attr_reader :key, :direction

  def initialize(key, direction)
    @key = key
    @direction = direction
  end

  def compare(a, b)
    a_value = a.fetch(key, 0)
    b_value = b.fetch(key, 0)

    if a_value < b_value
      direction == 'asc' ? -1 : 1
    elsif a_value > b_value
      direction == "asc" ? 1 : -1
    else
      0
    end
  end
end

def assert_equal(x, y)
  raise "#{x} not equal to #{y}" unless x == y
end

def test_min_by_key
  assert_equal({"a" => 1, "b" => 2}, min_by_key("a", [{"a" => 1, "b" => 2}, {"a" => 2}]))
  assert_equal({"a" => 1, "b" => 2}, min_by_key("a", [{"a" => 2}, {"a" => 1, "b" => 2}]))
  assert_equal({"a" => 2}, min_by_key("b", [{"a" => 1, "b" => 2}, {"a" => 2}]))
  assert_equal({}, min_by_key("a", [{}]))
  assert_equal({"b" => -1}, min_by_key("b", [{"a" => -1}, {"b" => -1}]))
  puts "test_min_by_key all passed!"
end

def test_first_by_key
  assert_equal(first_by_key("a", "asc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]), {"b" => 1}) # {"b" => -2} is also okay)
  assert_equal(first_by_key("a", "desc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]), {"a" => 10})
  assert_equal(first_by_key("b", "asc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]), {"b" => -2})
  assert_equal(first_by_key("b", "desc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]), {"b" => 1})
  assert_equal(first_by_key("a", "desc", [{}, {"a" => 10, "b" => -10}, {}, {"a" => 3, "c" => 3}]), {"a" => 10, "b" => -10}) 
  puts "test_first_by_key all passed!"
end

def test_record_comparator
  cmp = Comparator.new("a", "asc")
  assert_equal(cmp.compare({"a" =>1}, {"a" =>2}), -1)
  assert_equal(cmp.compare({"a" =>2}, {"a" =>1}), 1)
  assert_equal(cmp.compare({"a" =>1}, {"a" =>1}), 0)
  assert_equal(cmp.compare({"a" =>1}, {"b" =>1}), 1)
  
  cmp2 = Comparator.new("a", "desc")
  assert_equal(cmp2.compare({"a" =>1}, {"a" =>2}), 1)
  assert_equal(cmp2.compare({"a" =>2}, {"a" =>1}), -1)
  assert_equal(cmp2.compare({"a" =>1}, {"a" =>1}), 0)
  assert_equal(cmp2.compare({"a" =>1}, {"b" =>1}), -1)
  puts "test_record_comparator all passed!"
end

test_min_by_key
test_first_by_key
test_record_comparator
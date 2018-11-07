# frozen_string_literal: true

require 'minitest/autorun'
require_relative './next_server_number'

class NextServerNumberTest < Minitest::Test
  def test_next_number
    number = NextServerNumber.new

    assert_equal 1, number.next_number
    assert_equal 1, number.next_number(nums: [])
    assert_equal 3, number.next_number(nums: [1, 2])
    assert_equal 2, number.next_number(nums: [1, 5])
  end
end

#
# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# For example, Given s = “eceba”,

# T is "ece" which its length is 3.
#
# @param {String} s
# @return {Integer}


def longest_substring_with_at_most_two_repeated_chars(s)
  i = 0
  left = 0
  max_len = 0

  count_map = Hash.new(0)

  while i < s.length
    ch = s[i]
    if count_map.key?(ch)
      count_map[ch] += 1
    else
      count_map[ch] = 1
    end

    while count_map.keys.size > 2
      left_ch = s[left]

      if count_map.key?(left_ch)
        count_map[left_ch] -= 1
        count_map.delete(left_ch) if count_map[left_ch] == 0
      end

      left += 1
    end

    max_len = [max_len, i - left + 1].max
    i += 1
  end

  max_len
end

s = "abaac"
puts longest_substring_with_at_most_two_repeated_chars(s)

s = "aaaabbb"
puts longest_substring_with_at_most_two_repeated_chars(s)
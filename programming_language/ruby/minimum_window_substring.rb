# http://articles.leetcode.com/finding-minimum-window-in-s-which
#Given a set T of characters and a string S, find the minimum window in S which will contain all the characters in T in complexity O(n).

#eg,
#S = “ADOBECODEBANC”
# T = “ABC”

# Minimum window is “BANC”.
#
#
#
# The idea:
# We use a hash to save
# 1. key - which char we need to find
# 2. value - how many of this char we need to find
#
# The effective_count:
# When we find a char, if we need this char to satisfy the occurance of char in T, then we update the effective_count.
# If not, we don't update the effective_count

def minimum_window_substring(s, t)
  i = 0
  dict = Hash.new(0)

  while i < t.length
    ch = t[i]
    if dict.key?(ch)
      dict[ch] += 1
    else
      dict[ch] = 1
    end

    i += 1
  end

  right = 0
  left = 0
  min_start = 0
  min_len = s.length + 1
  effective_count = 0

  while right < s.length
    sch = s[right]

    if dict.key?(sch)
      # The effective_count:
      # When we find a char, if we need this char to satisfy the occurance of char in T, then we update the effective_count.
      # If not, we don't update the effective_count
      effective_count += 1 if dict[sch] > 0
      dict[sch] -= 1
    end

    while effective_count == t.length
      if right - left + 1 < min_len
        min_start = left
        min_len = right - left + 1
      end

      left_ch = s[left]

      if dict.key?(left_ch)
        dict[left_ch] += 1
        # if dict[left_ch] <= 0, it means this left_ch in S is just some extra ch,
        # which we don't necessarily need in order to satisfy the occurance of char in T
        effective_count -= 1 if dict[left_ch] > 0
      end
      left += 1
    end

    right += 1
  end

  if min_len == s.length + 1
    return ""
  else
    return s[min_start, min_len]
  end
end

s = "ADOBECODEBANC"
t = "ABC"

puts minimum_window_substring(s, t)
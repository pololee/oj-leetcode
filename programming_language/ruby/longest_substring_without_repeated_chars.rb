# @param {String} s
# @return {Integer}
#
# Use a hash table to save the occurance of an char.
# If found the char exists in the table, then move the left index to the position
# after the saved index in the table, and update the occurance index of this char in the table.

def length_of_longest_substring(s)
  i = 0
  j = 0
  char_table = {}

  longest_length = 0

  while j < s.length
    # if this char exists in the table, move the left index to the postion after the saved index
    # of this char in the table.
    if char_table.has_key?(s[j])
      i = char_table[s[j]] + 1
    end

    # Even if char_table has it, need to update its new index in the new substring
    char_table[s[j]] = j
    longest_length = [ j - i + 1, longest_length].max
    j += 1
  end

  longest_length
end

s = 'abcabcbb'
puts length_of_longest_substring(s)

s = "bbbbbbb"
puts length_of_longest_substring(s)

s = 'abcdefg'
puts length_of_longest_substring(s)
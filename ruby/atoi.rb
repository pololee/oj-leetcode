# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases.
# If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# # @param {String} str
# @return {Integer}
#
MAX_INT = 2147483647
MIN_INT = -1 * 2147483648
MAX_INT_DIV_TEN = 214748364

def my_atoi(str)
  i = 0
  # skip all the leading spaces
  while i < str.length && str[i] == ' '
    i += 1
  end

  # get the sign
  sign = 1
  if i < str.length && str[i] == '+'
    i += 1
  elsif i < str.length && str[i] == '-'
    sign = -1
    i += 1
  end

  num = 0
  while i < str.length && str[i] >= '0' && str[i] <= '9'
    digit = str[i].to_i
    puts digit
    if num > MAX_INT_DIV_TEN || num == MAX_INT_DIV_TEN && digit >= 8
      return sign == 1 ? MAX_INT : MIN_INT
    end
    num = num * 10 + digit
    i += 1
    puts num
  end

  (sign * num).to_i
end

# str = '           2147483647'
# puts str
# puts my_atoi(str)

# str = '                       -2147483647'
# puts str
# puts my_atoi(str)

# str = '   ='
# puts str
# puts my_atoi(str)

puts my_atoi("2147483648")
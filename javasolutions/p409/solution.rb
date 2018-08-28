# @param {String} s
# @return {Integer}
def longest_palindrome(s)
  table = Hash.new { |hash, key| hash[key] = 0 }

  s.chars.each do |ch|
    table[ch] += 1
  end

  length = 0
  table.each do |_, value|
    if value % 2 == 0
      length += value
    else
      length += (value - 1)
    end
  end

  length == s.size ? length : length + 1
end

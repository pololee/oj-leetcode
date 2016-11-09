# Implement strStr().

# Returns the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  if needle.length == 0
    return 0
  elsif haystack.length < needle.length
    # haystack.length == 0 included
    return -1
  else
    starter = 0
    j = 0

    while j < needle.length
      if haystack.length - starter < needle.length
        return -1
      elsif haystack[starter + j] != needle[j]
        j = 0
        starter += 1
      else
        j += 1
        return starter if j == needle.length
      end
    end
  end
end

def better_str_str(haystack, needle)
  (0..haystack.length).each do |starter|
    (0..needle.length).each do |j|
      return starter if j == needle.length
      return -1 if starter + j == haystack.length
      break if haystack[starter + j] != needle[j]
    end
  end
end

# test
puts "needle empty"
puts str_str('haystack', '')
puts better_str_str('haystack', '')

puts "haystack is shorter than needle"
puts str_str('str', 'strstr')
puts better_str_str('str', 'strstr')

puts "no match"
puts str_str('stististi', 'str')
puts better_str_str('stististi', 'str')

puts "match"
puts str_str('stistrstr', 'str')
puts better_str_str('stistrstr', 'str')

puts "match end"
puts str_str('stististr', 'str')
puts better_str_str('stististr', 'str')

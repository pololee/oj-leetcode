
# Similar to Question [6. Reverse Words in a String], but with the following constraints:
# “The input string does not contain leading or trailing spaces and the words
# are always separated by a single space.”
# Could you do it in-place without allocating extra space?

# This is very important
# a' = a
# (ab)' = b'a'
# we want ab -> ba
# ab -> b'a'(by reverse the entire word) -> ba(by reverse each word)
#
# Since this is ruby, we are not able to pass by reference.

def reverseWordsII(str)
  @str = str
  reverse(0, @str.length - 1)

  i = 0
  word_start = 0
  while i <= @str.length
    if @str[i] == ' ' || i == @str.length
      reverse(word_start, i - 1)
      word_start = i + 1
    end
    i += 1
  end

  @str
end

def reverse(start_idx, end_idx)
  temp = ''

  i = 0
  while i < (end_idx - start_idx + 1) / 2
    temp = @str[start_idx + i]
    @str[start_idx + i] = @str[end_idx - i]
    @str[end_idx - i] = temp
    i += 1
  end
end

test_str = 'the sky is blue'
puts test_str
puts reverseWordsII(test_str)

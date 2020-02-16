# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
#
# Example Questions Candidate Might Ask:
# Q: What constitutes a word?
# A: A sequence of non-space characters constitutes a word.
# Q: Does tab or newline character count as space characters?
# A: Assume the input does not contain any tabs or newline characters.
# Q: Could the input string contain leading or trailing spaces?
# A: Yes. However, your reversed string should not contain leading or trailing spaces.
# Q: How about multiple spaces between two words?
# A: Reduce them to a single space in the reversed string.

def reverseWords(str)
  new_str = ''
  word_end = str.length

  i = str.length - 1
  while i >= 0
    if str[i] == ' '
      word_end = i
    elsif str[i - 1] == ' ' || i == 0
      new_str.concat(' ') if new_str.length != 0
      new_str.concat(str[i..(word_end - 1)])
    end
    i -= 1
  end

  new_str
end

test = '  the  sky is blue.  '
puts test
puts reverseWords(test)

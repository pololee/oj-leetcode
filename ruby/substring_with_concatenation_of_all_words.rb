# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter).

def substring_with_concatenation_of_all_words(s, words)
  return [] if words.size == 0 || s.length == 0

  wordLen = words[0].length
  numOfWords = words.size
  totalLen = wordLen * numOfWords

  wordsMap = Hash.new(0)
  words.each do |w|
    if wordsMap.key?(w)
      wordsMap[w] += 1
    else
      wordsMap[w] = 1
    end
  end

  i = 0
  subsPos = []
  stringMap = Hash.new(0)

  while i + totalLen <= s.length
    stringMap.clear
    j = i

    while j < i + totalLen
      subs = s[j, wordLen]

      if wordsMap.key?(subs)
        if stringMap.key?(subs)
          stringMap[subs] += 1
          break if stringMap[subs] > wordsMap[subs]
        else
          stringMap[subs] = 1
        end
      else
        break
      end

      j += wordLen
    end

    subsPos << i if j == i + totalLen
    i += 1
  end

  subsPos
end

s = "barfoothefoobarman"
t = ["foo", "bar"]

puts substring_with_concatenation_of_all_words(s, t)
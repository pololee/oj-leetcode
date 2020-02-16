def alnum?(ch)
  /[[:alnum:]]/ =~ ch
end

def palindrome?(str)
  l = 0
  r = str.length - 1

  while l < r
    while l < r && !alnum?(str[l])
      l += 1
    end

    while l < r && !alnum?(str[r])
      r -= 1
    end

    return false unless str[l].downcase == str[r].downcase

    l += 1
    r -= 1
  end

  return true
end


str1 = 'A man, a plan, a canal: Panama'
str2 = 'race a car'

puts palindrome?(str1)
puts palindrome?(str2)

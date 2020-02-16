def is_number(str)
  i = 0
  n = str.length

  # Skip all the leading spaces
  while i < n && str[i] == ' '
    i += 1
  end

  # pass the sign
  if i < n && (str[i] == '+' || str[i] == '-')
    i += 1
  end

  # pass all the numbers before decimal point (dot)
  conclusion = false
  while i < n && is_digit(str[i])
    i += 1
    conclusion = true
  end

  if i < n && str[i] == '.'
    i += 1

    # numbers after dot is not necessary, so we don't update conclusion = false here
    # Just pass all the numbers after dot
    while i < n && is_digit(str[i])
      i += 1
      conclusion = true
    end
  end

  # pass the number, either decimal or integer before 'e'
  if conclusion && i < n && str[i] == 'e'
    i += 1

    # numbers after 'e' is required, otherwise, it's not valid.
    # So we update conclusion to be false here.
    conclusion = false
    if i < n && (str[i] == '+' || str[i] == '-')
      i += 1
    end
    while i < n && is_digit(str[i])
      i += 1
      conclusion = true
    end
  end

  # pass all the trailing spaces
  while i < n && str[i] == ' '
    i += 1
  end

  conclusion && i == n
end

def is_digit(char)
  char >= '0' && char <= '9'
end

str = '      1.0e10  '
puts is_number(str)

str = '   1.0a'
puts is_number(str)
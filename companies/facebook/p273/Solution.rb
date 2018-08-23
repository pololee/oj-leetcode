def read_number(n, result = '', base = 10**9)
  return result if n == 0

  quotient = n/base
  if quotient != 0
    tmp_result = resolve_triples(quotient) + " " + resolve_thousand_base(base)
    read_number(n - quotient * base, result + " " + tmp_result, base/(10**3))
  else
    read_number(n, result, base/(10**3))
  end
end

def resolve_thousand_base(base)
  case base
  when 10**9
    'billion'
  when 10**6
    'million'
  when 10**3
    'thousand'
  else
    ''
  end
end

def resolve_triples(n, result = '', base = 100)
  return result if n == 0

  quotient = n/base
  if quotient != 0
    if base == 10
      if quotient == 1
        tmp_result = resolve_base(n, base)
        resolve_triples(0, result + " " + tmp_result, base/100)
      else
        tmp_result = resolve_base(quotient, base)
        resolve_triples(n - quotient * base, result + " " + tmp_result, base/10)
      end
    else
      tmp_result = resolve_base(quotient, base)
      resolve_triples(n - quotient * base, result + " " + tmp_result, base/10)
    end
  else
    resolve_triples(n, result, base/10)
  end
end

def resolve_base(result, base)
  if base == 100
    HundredResolver.resolve(result)
  elsif base == 10
    if result > 10
      TensResolver.resolve(result)
    else
      TentiesResolver.resolve(result)
    end
  elsif base == 1
    OnesResolver.resolve(result)
  end
end

class OnesResolver
  def self.resolve(n)
    case n
    when 1
      'one'
    when 2
      'two'
    when 3
      'three'
    when 4
      'four'
    when 5
      'five'
    when 6
      'six'
    when 7
      'seven'
    when 8
      'eight'
    when 9
      'nine'
    end
  end
end

class TensResolver
  def self.resolve(n)
    case n
    when 10
      'ten'
    when 11
      'eleven'
    when 12
      'twelve'
    when 13
      'thirteen'
    when 14
      'fourteen'
    when 15
      'fifteen'
    when 16
      'sixteen'
    when 17
      'seventeen'
    when 18
      'eighteen'
    when 19
      'nineteen'
    end
  end
end

class TentiesResolver
  def self.resolve(n)
    case n
    when 2
      'tweenty'
    when 3
      'thirty'
    when 4
      'forty'
    when 5
      'fifty'
    when 6
      'sixty'
    when 7
      'seventy'
    when 8
      'eighty'
    when 9
      'ninety'
    end
  end
end

class HundredResolver
  def self.resolve(n)
    OnesResolver.resolve(n) + " " + 'hundred'
  end
end


puts read_number(123)
puts read_number(12345)
puts read_number(1234567)
class Permutation
  def permute(str)
    return [] if str.empty?
    answer = []
    recursive_permute('', str, answer)
    answer
  end

  def recursive_permute(so_far, rest, answer)
    if rest.empty?
      answer << so_far
    else
      rest.chars.each_with_index do |_, idx|
        remaining = rest[0, idx - 0] + rest[idx + 1, rest.length]
        recursive_permute(so_far + rest[idx], remaining, answer)
      end
    end
  end
end

per = Permutation.new
puts per.permute('abc')

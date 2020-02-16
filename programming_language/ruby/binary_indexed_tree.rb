class BinaryIndexTree
  def initialize(input_arry)
    @length = input_arry.length
    @bit = Array.new(@length + 1){0}

    input_arry.each_index { |i| update(i, input_arry[i]) }
  end

  def update(idx, x)
    index = idx + 1

    while index <= @length
      @bit[index] += x
      index += last_set_bit(index)
    end
  end

  def sum(idx)
    index = idx + 1
    ans = 0

    while index != 0
      ans += @bit[index]
      index -= last_set_bit(index)
    end

    ans
  end

  def get_tree
    @bit
  end

  private

  def last_set_bit(x)
    x & (-x)
  end
end

bit = BinaryIndexTree.new([5, 1, 15, 11, 52, 28, 0])
puts bit.get_tree

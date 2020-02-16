class TwoSum

  def initialize
    @h = Hash.new(0)
  end

  def add(input)
    @h[input] += 1
  end

  def find(target)
    @h.each do |k, v|
      if k == target - k
        return true if @h[k] > 1
      else
        return true if @h[target - k] > 0
      end
    end

    return false
  end
end

ts = TwoSum.new
ts.add(1)
ts.add(3)
ts.add(5)
puts ts.find(4)
puts ts.find(7)
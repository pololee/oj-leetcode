class WeightedIntervalScheduling
  
  class Request < Struct.new(:startTime, :endTime, :value, :closet_disjoint_request_index)
  end

  attr_reader :solutions

  def initialize
    @requests = set_up_requests
    @solutions = [0]
  end

  def compute_iterative
    (1..@requests.length-1).each do |index|
      current = @requests[index]
      @solutions[index] = [current.value + @solutions[current.closet_disjoint_request_index], @solutions[index - 1]].max
    end
  end

  def compute_recursive(index = @requests.length - 1)
    if index == 0
      return 0
    elsif !@solutions[index].nil?
      return @solutions[index]
    else
      current = @requests[index]
      include_current = current.value + compute_recursive(current.closet_disjoint_request_index)
      exclude_current = compute_recursive(index - 1)
      @solutions[index] = [include_current, exclude_current].max
      return @solutions[index]
    end
  end

  private

  def set_up_requests
    requests = []
    requests << Request.new(0, 0, 0, 0) # dummy first element to make life easier
    requests << Request.new(1, 5, 2, 0)
    requests << Request.new(2, 8, 4, 0)
    requests << Request.new(6, 10, 4, 1)
    requests << Request.new(3, 14, 7, 0)
    requests << Request.new(12, 20, 2, 3)
    requests << Request.new(13, 21, 1, 3)
    requests
  end
end

scheduler = WeightedIntervalScheduling.new
scheduler.compute_iterative
puts scheduler.solutions.inspect

scheduler2 = WeightedIntervalScheduling.new
scheduler2.compute_recursive
puts scheduler2.solutions.inspect

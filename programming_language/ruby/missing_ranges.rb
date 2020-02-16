# Given a sorted integer array where the range of elements are [lower, upper]
# inclusive, return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
# "4->49", "51->74", "76->99"].
#
# Idea:
# Add two "artificial" elements, lower -1 before the first element and upper + 1
# after the last element

def missing_ranges(array, lower = 0, upper = 99)
  ranges = []

  i = 0
  prev = lower - 1

  while i <= array.size
    curr = (i == array.size) ? upper + 1 : array[i]

    if curr - prev > 1
      ranges << get_range(prev + 1, curr - 1)
    end

    prev = curr
    i += 1
  end

  ranges
end

def get_range(from, to)
  from == to ? "#{from}" : "#{from}->#{to}"
end

a = [0, 1, 3, 50, 75]
puts missing_ranges(a)
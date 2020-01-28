class Entry
  attr_reader :value, :timestamp

  def initialize(value, timestamp)
    @value = value
    @timestamp = timestamp
  end
end

class TimeMap
  attr_reader :table

  def initialize
    @table = {}
  end

  def set(key, value, timestamp)
    entry = Entry.new(value, timestamp)

    if table.key?(key)
      table[key].add(entry)
    else
      table[key] = [entry]
    end
  end

  def get(key, timestamp)
    return '' unless table.key?(key)

    entries = table[key]
    idx = entries.bsearch_index { |x| x.timestamp > timestamp }

    return entries[-1].value if idx.nil?
    return '' if idx.zero?

    entries[idx - 1].value
  end
end

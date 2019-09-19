### [981\. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

# Difficulty: **Medium**

# Create a timebased key-value store class `TimeMap`, that supports two operations.

# 1\. `set(string key, string value, int timestamp)`

# *   Stores the `key` and `value`, along with the given `timestamp`.

# 2\. `get(string key, int timestamp)`

# *   Returns a value such that `set(key, value, timestamp_prev)` was called previously, with `timestamp_prev <= timestamp`.
# *   If there are multiple such values, it returns the one with the largest `timestamp_prev`.
# *   If there are no values, it returns the empty string (`""`).

# **Example 1:**

# ```
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:  
# TimeMap kv;  
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1  
# kv.get("foo", 1);  // output "bar"  
# kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"  
# kv.set("foo", "bar2", 4);  
# kv.get("foo", 4); // output "bar2"  
# kv.get("foo", 5); //output "bar2"  

# ```

# **Example 2:**

# ```
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]
# ```

# **Note:**

# 1.  All key/value strings are lowercase.
# 2.  All key/value strings have length in the range `[1, 100]`
# 3.  The `timestamps` for all `TimeMap.set` operations are strictly increasing.
# 4.  `1 <= timestamp <= 10^7`
# 5.  `TimeMap.set` and `TimeMap.get` functions will be called a total of `120000` times (combined) per test case.

#### Solution

class Entry
  attr_reader :value, :timestamp

  def initialize(value, timestamp)
    @value = value
    @timestamp = timestamp
  end
end

class TimeMap
  #   Initialize your data structure here.
  attr_reader :table

  def initialize
    @table = {}
  end

  #   :type key: String
  #   :type value: String
  #   :type timestamp: Integer
  #   :rtype: Void
  def set(key, value, timestamp)
    if table.key?(key)
      table[key].push(Entry.new(value, timestamp))
    else
      table[key] = [Entry.new(value, timestamp)]
    end
  end

  #   :type key: String
  #   :type timestamp: Integer
  #   :rtype: String
  def get(key, timestamp)
    return '' unless table.key?(key)

    entries = table[key]
    idx = entries.bsearch_index { |x| x.timestamp > timestamp }

    return entries[-1].value if idx.nil?
    return '' if idx.zero?

    entries[idx - 1].value
  end
end

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap.new()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)

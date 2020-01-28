class Logger
  attr_reader :msg_map
  def initialize
    @msg_map = {}
  end

  def should_print_message(timestamp, message)
    return false if timestamp < msg_map.fetch(message, 0)

    msg_map[message] = timestamp + 10
    true
  end

  def should_print_message_2(timestamp, message)
    return false if msg_map.key?(message) && msg_map[message] + 10 > timestamp

    msg_map[message] = timestamp
    true
  end
end
# Your Logger object will be instantiated and called as such:
# obj = Logger.new()
# param_1 = obj.should_print_message(timestamp, message)

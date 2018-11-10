# frozen_string_literal: true

require 'set'
require_relative './next_server_number'

class HostNameError < StandardError; end

class ServerManager
  attr_reader :host_table, :next_server_number

  HOST_NAME_REGEX = /^([a-zA-Z]+)(\d+)$/

  def initialize
    @host_table = {}
    @next_server_number = NextServerNumber.new
  end

  def allocate(host_type:)
    if host_table.key?(host_type)
      number = next_server_number.next_number(nums: host_table.fetch(host_type))
      host_table[host_type].add(number)
      "#{host_type}#{number}"
    else
      host_table[host_type] = Set.new([1])
      "#{host_type}1"
    end
  end

  def deallocate(hostname:)
    hostname = hostname.strip
    parsed = parse_hostname(hostname)
    host_type = parsed[0]
    server_number = parsed[1].to_i

    return unless host_table.key?(host_type) && host_table[host_type].member?(server_number)
    host_table[host_type].delete(server_number)
    host_table.delete(host_type) if host_table[host_type].empty?
  end

  private

  def parse_hostname(hostname)
    result = HOST_NAME_REGEX.match(hostname)
    raise HostNameError.new("incorrect format #{hostname}") unless result&.size == 3

    result[1..2]
  end
end

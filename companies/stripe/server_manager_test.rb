# frozen_string_literal: true

require 'minitest/autorun'
require_relative './server_manager'

class ServerManagerTest < Minitest::Test
  def test_allocate
    manager = ServerManager.new

    assert_equal 'apibox1', manager.allocate(host_type: 'apibox')
    assert_equal 'apibox2', manager.allocate(host_type: 'apibox')

    manager.deallocate(hostname: 'apibox1')
    assert_equal 'apibox1', manager.allocate(host_type: 'apibox')
  end

  def test_deallocate__hostname_incorrect_format
    manager = ServerManager.new

    assert_raises HostNameError do
      manager.deallocate(hostname: '~jkd0~947')
    end
  end

  def test_deallocate__host_type_not_exist
    manager = ServerManager.new

    manager.deallocate(hostname: 'apibox1')
  end

  def test_deallocate
    manager = ServerManager.new
    name = manager.allocate(host_type: 'apibox')
    manager.deallocate(hostname: name)

    refute manager.host_table.key?('apibox')
  end
end

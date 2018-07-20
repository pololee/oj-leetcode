class ListNode
  attr_accessor :val, :next

  def initialize(x)
    @val = x
    @next = nil
  end
end

def reverse_list(previous, current)
  if current.next.nil?
    current.next = previous
    return current
  end

  new_head = reverse_list(current, current.next)
  current.next = previous

  return new_head
end

head = ListNode.new(1)
head.next = ListNode.new(2)
head.next.next = ListNode.new(3)
head.next.next.next = ListNode.new(4)
new_head = reverse_list(nil, head)
p new_head.val
p new_head.next.val
p new_head.next.next.val
p new_head.next.next.next.val

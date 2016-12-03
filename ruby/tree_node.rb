class TreeNode

  attr_accessor :data, :left, :right

  def initialize(data)
    @data = data
  end
end

def pre_order_traverse(node, output)
  if node.nil?
    return ""
  end

  output = "#{node.data} "
  output += pre_order_traverse(node.left, output)
  output += pre_order_traverse(node.right, output)
  output
end

def in_order_traverse(node, output)
  if node.nil?
    return ''
  end

  output = in_order_traverse(node.left, output)
  output += "#{node.data} "
  output += in_order_traverse(node.right, output)
  output
end

def post_order_traverse(node, output)
  if node.nil?
    return ""
  end

  output = post_order_traverse(node.left, output)
  output += post_order_traverse(node.right, output)
  output += "#{node.data} "
  output
end

def test
  root = TreeNode.new('A')
  root.left = TreeNode.new('B')
  root.right = TreeNode.new('C')

  root.left.left = TreeNode.new('D')
  root.left.right = TreeNode.new('E')
  root.right.right = TreeNode.new('F')

  root.left.right.left = TreeNode.new('G')
  output = ''
  puts pre_order_traverse(root, output)
  output = ''
  puts in_order_traverse(root, output)
  output = ''
  puts post_order_traverse(root, output)
end

test
package javasolutions.learn;

public class BTNode<T> {
	// package-private
	T data;
	BTNode<T> left, right;

	public BTNode(T dataInput, BTNode<T> leftNode, BTNode<T> rightNode) {
		data = dataInput;
		left = leftNode;
		right = rightNode;
	}

	public BTNode(T dataInput) {
		this(dataInput, null, null);
	}

	public String toString() {
		return data.toString();
	}

	public static void main(String[] args) {
		BTNode<Integer> a = new BTNode<Integer>(10);
		System.out.println("a: " + a.toString());
		BTNode<Integer> b = new BTNode<Integer>(100);
		System.out.println("b: " + b.toString());
		BTNode<Integer> c = new BTNode<Integer>(1000, a, b);
		System.out.println("c: " + c.toString());
		System.out.println("c.left: " + c.left.toString());
		System.out.println("c.right: " + c.right.toString());
	}
}
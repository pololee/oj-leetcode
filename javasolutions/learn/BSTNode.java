package javasolutions;

public class BSTNode<T> {
	// package-private
	T data;
	BSTNode<T> left, right;

	public BSTNode(T dataInput, BSTNode<T> leftNode, BSTNode<T> rightNode) {
		data = dataInput;
		left = leftNode;
		right = rightNode;
	}

	public BSTNode(T dataInput) {
		this(dataInput, null, null);
	}

	public String toString() {
		return data.toString();
	}

	public static void main(String[] args) {
		BSTNode<Integer> a = new BSTNode<Integer>(10);
		System.out.println("a: " + a.toString());
		BSTNode<Integer> b = new BSTNode<Integer>(100);
		System.out.println("b: " + b.toString());
		BSTNode<Integer> c = new BSTNode<Integer>(1000, a, b);
		System.out.println("c: " + c.toString());
		System.out.println("c.left: " + c.left.toString());
		System.out.println("c.right: " + c.right.toString());
	}
}
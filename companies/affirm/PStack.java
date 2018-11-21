public class PStack {
  private int size;
  private int value;
  private PStack prev;

  public PStack() {
    this.prev = null;
    this.value = 0;
    this.size = 0;
  }

  public PStack(PStack prev, int value, int size) {
    this.prev = prev;
    this.value = value;
    this.size = size;
  }

  public PStack push(int value) {
    return new PStack(this, value, this.size + 1);
  }

  public PStack pop() {
    return prev;
  }

  public int size() {
    return size;
  }

  public int peek() {
    return value;
  }

  public static void main(String[] args) {
    PStack p = new PStack();
    System.out.println(p.size());

    PStack s1 = p.push(1);
    PStack s2 = s1.push(2);
    PStack s3 = s2.push(3);
    System.out.println(String.format("peek %d", s3.peek()));
    System.out.println(String.format("size %d", s3.size()));

    PStack tmp = s3.pop();
    System.out.println(tmp == s2);
  }
}

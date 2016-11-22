// http://www.journaldev.com/1663/java-generics-example-method-class-interface
package javasolutions.learn;

public class GenericsType<T> {
  private T t;

  public T get() {
    return this.t;
  }

  private void set(T input) {
    this.t = input;
  }

  public static void main(String[] args) {
    GenericsType<String> type = new GenericsType<> ();
    type.set("some");
    System.out.println(type.get());

    // GenericsType type1 = new GenericsType(); //raw type
    // type1.set("Pankaj"); //valid
    // type1.set(10); //valid and autoboxing support
  }
}
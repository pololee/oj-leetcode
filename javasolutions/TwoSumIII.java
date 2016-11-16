import java.util.HashMap;

public class TwoSumIII {
  private HashMap<Integer, Integer> store = new HashMap<Integer, Integer>();

  public void add(int input) {
    if (store.containsKey(input)) {
      store.put(input, store.get(input) + 1);
    } else {
      store.put(input, 1);
    }
  }

  public boolean find(int value) {
    for (Integer key : store.keySet()) {
      if (store.containsKey(value - key)) {
        if (key != (value - key)) {
          return true;
        } else if (store.get(key) > 1) {
          return true;
        }
      }
    }

    return false;
  }

  public static void main(String[] args) {
    TwoSumIII twoSum = new TwoSumIII();

    twoSum.add(1);
    twoSum.add(3);
    twoSum.add(5);
    System.out.println(twoSum.find(4));
    System.out.println(twoSum.find(7));
  }
}

import java.util.*;

public class FindRecordSolution {
  public static Map<String, Integer> minByKey(String key, List<Map<String, Integer>> records) {
    // write your code
    return firstByKey(key, "asc", records);
  }

  public static Map<String, Integer> firstByKey(String key, String direction, List<Map<String, Integer>> records) {
    // write your code
    if(records.isEmpty()) {
      return new HashMap<String, Integer>();
    }

    Comparator cmp = new Comparator(key, direction);
    Map<String, Integer> ans = records.get(0);

    for(int i = 0; i < records.size(); i++) {
      Map<String, Integer> curr = records.get(i);
      if(cmp.compare(curr, ans) < 0) {
        ans = curr;
      }
    }

    return ans;
  }

  static class Comparator {
    String key;
    String direction;

    Comparator(String key, String direction) {
      this.key = key;
      this.direction = direction;
    }

    int compare(Map<String, Integer> a, Map<String, Integer> b) {
      Integer aValue = a.getOrDefault(key, 0);
      Integer bValue = b.getOrDefault(key, 0);

      if(aValue < bValue) {
        return direction == "asc" ? -1 : 1;
      } else if (aValue > bValue) {
        return direction == "asc" ? 1 : -1;
      }

      return 0;
    }
  }

  public static void assertEqual(Map<String, Integer> a, Map<String, Integer> b) throws Exception {
    if(a.size() != b.size()) {
      throw new Exception("not equal");
    }

    for(String key : a.keySet()) {
      if(!b.containsKey(key) || a.get(key) != b.get(key)) {
        throw new Exception("not equal");
      }
    }
  }

  public static void assertIntEqual(Integer x, Integer y) throws Exception {
    if(x != y) {
      throw new Exception("int not equal");
    }
  }

  public static void testMinByKey() throws Exception {
    // "a", [{"a" => 1, "b" => 2}, {"a" => 2}]
    // {"a" => 1, "b" => 2}
    List<Map<String, Integer>> t1 = new ArrayList<>();
    Map<String, Integer> t11 = new HashMap<>();
    t11.put("a", 1);
    t11.put("b", 2);
    t1.add(t11);
    Map<String, Integer> t12 = new HashMap<>();
    t12.put("a", 2);
    t1.add(t12);

    assertEqual(t1.get(0), minByKey("a", t1));

    // "a", [{"a" => 2}, {"a" => 1, "b" => 2}]
    // {"a" => 1, "b" => 2}
    List<Map<String, Integer>> t2 = new ArrayList<>();
    Map<String, Integer> t21 = new HashMap<>();
    t21.put("a", 2);
    t2.add(t21);
    Map<String, Integer> t22 = new HashMap<>();
    t22.put("a", 1);
    t22.put("b", 2);
    t2.add(t22);

    assertEqual(t2.get(1), minByKey("a", t2));

    // "b", [{"a" => 1, "b" => 2}, {"a" => 2}]
    // {"a" => 2}
    List<Map<String, Integer>> t3 = new ArrayList<>();
    Map<String, Integer> t31 = new HashMap<>();
    t31.put("a", 1);
    t31.put("b", 2);
    t3.add(t31);
    Map<String, Integer> t32 = new HashMap<>();
    t32.put("a", 2);
    t3.add(t32);

    assertEqual(t3.get(1), minByKey("b", t3));

    // "a", [{}]
    // {}
    List<Map<String, Integer>> t4 = new ArrayList<>();
    Map<String, Integer> t41 = new HashMap<>();
    t4.add(t41);

    assertEqual(t4.get(0), minByKey("a", t4));

    // "b", [{"a" => -1}, {"b" => -1}]
    // {"b" => -1}
    List<Map<String, Integer>> t5 = new ArrayList<>();
    Map<String, Integer> t51 = new HashMap<>();
    t51.put("a", -1);
    t5.add(t51);
    Map<String, Integer> t52 = new HashMap<>();
    t52.put("b", -1);
    t5.add(t52);

    assertEqual(t5.get(1), minByKey("b", t5));

    System.out.println("test minByKey All Passed!");
  }

  public static void testFirstByKey() throws Exception {
    // "a", "asc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]
    List<Map<String, Integer>> t1 = new ArrayList<>();
    Map<String, Integer> t11 = new HashMap<>();
    t11.put("b", 1);
    t1.add(t11);
    Map<String, Integer> t12 = new HashMap<>();
    t12.put("b", -2);
    t1.add(t12);
    Map<String, Integer> t13 = new HashMap<>();
    t13.put("a", 10);
    t1.add(t12);

    assertEqual(t1.get(0), firstByKey("a", "asc", t1)); // t1.get(1) is also okay

    // "a", "desc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]
    List<Map<String, Integer>> t2 = new ArrayList<>();
    Map<String, Integer> t21 = new HashMap<>();
    t21.put("b", 1);
    t2.add(t21);
    Map<String, Integer> t22 = new HashMap<>();
    t22.put("b", -2);
    t2.add(t22);
    Map<String, Integer> t23 = new HashMap<>();
    t23.put("a", 10);
    t2.add(t23);

    assertEqual(t2.get(2), firstByKey("a", "desc", t2));

    // "b", "asc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]
    List<Map<String, Integer>> t3 = new ArrayList<>();
    Map<String, Integer> t31 = new HashMap<>();
    t31.put("b", 1);
    t3.add(t31);
    Map<String, Integer> t32 = new HashMap<>();
    t32.put("b", -2);
    t3.add(t32);
    Map<String, Integer> t33 = new HashMap<>();
    t33.put("a", 10);
    t3.add(t33);

    assertEqual(t3.get(1), firstByKey("b", "asc", t3));

    // "b", "desc", [{"b" => 1}, {"b" => -2}, {"a" => 10}]
    List<Map<String, Integer>> t4 = new ArrayList<>();
    Map<String, Integer> t41 = new HashMap<>();
    t41.put("b", 1);
    t4.add(t41);
    Map<String, Integer> t42 = new HashMap<>();
    t42.put("b", -2);
    t4.add(t42);
    Map<String, Integer> t43 = new HashMap<>();
    t43.put("a", 10);
    t4.add(t43);

    assertEqual(t4.get(0), firstByKey("b", "desc", t4));

    // "a", "desc", [{}, {"a" => 10, "b" => -10}, {}, {"a" => 3, "c" => 3}]
    List<Map<String, Integer>> t5 = new ArrayList<>();
    t5.add(new HashMap<String, Integer>());
    Map<String, Integer> t51 = new HashMap<>();
    t51.put("a", 10);
    t51.put("b", -10);
    t5.add(t51);
    t5.add(new HashMap<String, Integer>());
    Map<String, Integer> t52 = new HashMap<>();
    t52.put("a", 3);
    t52.put("c", 3);
    t5.add(t52);

    assertEqual(t5.get(1), firstByKey("a", "desc", t5));
    System.out.println("test FirstByKey All Passed!");
  }

  public static void testComparator() throws Exception {
    Comparator cmp = new Comparator("a", "asc");

    Map<String, Integer> x = new HashMap<>();
    x.put("a", 1);
    Map<String, Integer> y = new HashMap<>();
    y.put("a", 2);
    assertIntEqual(-1, cmp.compare(x, y));

    Map<String, Integer> x1 = new HashMap<>();
    x1.put("a", 2);
    Map<String, Integer> y1 = new HashMap<>();
    y1.put("a", 1);
    assertIntEqual(1, cmp.compare(x1, y1));

    Map<String, Integer> x2 = new HashMap<>();
    x2.put("a", 1);
    Map<String, Integer> y2 = new HashMap<>();
    y2.put("a", 1);
    assertIntEqual(0, cmp.compare(x2, y2));

    Map<String, Integer> x3 = new HashMap<>();
    x3.put("a", 1);
    Map<String, Integer> y3 = new HashMap<>();
    y3.put("b", 1);
    assertIntEqual(1, cmp.compare(x3, y3));

    Comparator cmp2 = new Comparator("a", "desc");

    Map<String, Integer> m = new HashMap<>();
    m.put("a", 1);
    Map<String, Integer> n = new HashMap<>();
    n.put("a", 2);
    assertIntEqual(1, cmp2.compare(m, n));

    Map<String, Integer> m1 = new HashMap<>();
    m1.put("a", 2);
    Map<String, Integer> n1 = new HashMap<>();
    n1.put("a", 1);
    assertIntEqual(-1, cmp2.compare(m1, n1));

    Map<String, Integer> m2 = new HashMap<>();
    m2.put("a", 1);
    Map<String, Integer> n2 = new HashMap<>();
    n2.put("a", 1);
    assertIntEqual(0, cmp2.compare(m2, n2));

    Map<String, Integer> m3 = new HashMap<>();
    m3.put("a", 1);
    Map<String, Integer> n3 = new HashMap<>();
    n3.put("b", 1);
    assertIntEqual(-1, cmp2.compare(m3, n3));

    System.out.println("test Comparator All Passed!");
  }

  public static void main(String[] args) throws Exception {
    testMinByKey();
    testFirstByKey();
    testComparator();
  }
}

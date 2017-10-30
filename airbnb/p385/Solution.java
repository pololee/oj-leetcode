package airbnb.p385;

pubic class Solution {
  public NestedInteger deserialize(String s) {
    if (s.charAt(0) != '[') {
      return new NestedInteger(Integer.parseInt(s));
    }

    int start = 1;
    Stack<NestedInteger> stack = new Stack<>();

    for(int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);

      if (ch == '[') {
        stack.push(new NestedInteger());
        start = i + 1;
      } else if (ch == ',' || ch == ']') {
        if (i > start) {
          int number = Integer.parseInt(s.subString(start, i));
          stack.peek().add(new NestedInteger(number));
        }

        start = i + 1;

        if (ch == ']' && stack.size() > 1) {
          NestedInteger nested = stack.pop();
          stack.peek().add(nested);
        }
      }
    }

    return stack.peek();
  }
}
import java.util.*;

public class Factorial {
    /**
     * @param n: an integer
     * @return:  the factorial of n
     */
    public String factorial(int n) {
        // write your code here
        if(n == 0 || n == 1) return "1";
        
        List<Integer> ans = new ArrayList<>();
        ans.add(1);
        for(int x = 2; x <= n; x++) {
            multiply(ans, x);
        }
        
        StringBuilder builder = new StringBuilder();
        int size = ans.size();
        for(int i = size - 1; i >= 0; i--) {
            builder.append(ans.get(i));
        }
        
        return builder.toString();
    }
    
    private void multiply(List<Integer> ans, int x) {
        int carry = 0;
        int size = ans.size();
        
        for (int i = 0; i < size; i++) {
            int prod = ans.get(i) * x + carry;
            ans.set(i, prod % 10);
            carry = prod / 10;
        }

        
        while(carry != 0) {
            ans.add(carry % 10);
            carry = carry / 10;
        }
    }

    public static void main(String[] args) {
      int n = 4;
      Factorial sol = new Factorial();
      sol.factorial(n);
    }
}

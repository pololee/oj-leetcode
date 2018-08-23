package facebook.p277;

/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        if(n <= 0) return -1;
        
        int candidate = 0;
        for(int i = 0; i < n; i++) {
            if (knows(candidate, i)) {
                candidate = i;
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(i != candidate && !knows(i, candidate)) {
                return -1;
            }
            
            if(i < candidate && knows(candidate, i)) {
                return -1;
            }
        }
        
        return candidate;
    }
}
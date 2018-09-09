public class Solution {
   public String minWindow(String s, String t) {
       if (s.length() < t.length()){
           return “”;
       }

       int j = 0;
       int minlen = Integer.MAX_VALUE;
       String res = “”;
       int[] source = new int[256];
       int[] target = new int[256];
       initsource(target, t);

       for (int i = 0; i < s.length(); i++){
           while (j < s.length() && !isValid(source, target)){
               source[s.charAt(j)]++;
               j++;
           }

           if (isValid(source, target)){
               if (j - i < minlen){
                minlen = j - i;
                res = s.substring(i,j);
               }
           }

           source[s.charAt(i)] --;
       }

       return res;
   }

   public void initsource(int[] target, String t){
       for (int i = 0; i < t.length(); i++){
           target[t.charAt(i)]++;
       }
   }

   public boolean isValid(int[] source, int[] target){
       for (int i = 0; i < 256; i++){
           if (source[i] < target[i]){
               return false;
           }
       }

       return true;
   }

   public static void main(String[] args) {
     Solution sol = new Solution();
     System.out.printlnI(sol.minWindow("bca", "ba"));
   }
}

/**
 * https://leetcode.com/problems/maximum-product-of-word-lengths/?tab=Description
 *
 * Use binary bit as the hashmap for a word
 */
package javasolutions.p318;

public class MaxProductOfWordLengths {
  public int maxProduct(String[] words) {
    if (words.length == 0) return 0;

    int answer = 0;
    int[] masks = new int[words.length];

    for (int i = 0; i < words.length; i++) {

      for (char ch : words[i].toCharArray()) {
        masks[i] |= 1 << (ch - 'a');
      }

      for (int j = 0; j < i; j++) {
        if ((masks[j] & masks[i]) == 0) {
          answer = Math.max(answer, words[j].length() * words[i].length());
        }
      }
    }

    return answer;
  }
}
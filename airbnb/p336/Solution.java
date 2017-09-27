/**
https://leetcode.com/problems/palindrome-pairs/description/

Given a list of unique words, find all pairs of distinct indices (i, j) in 
the given list, so that the concatenation of the two words, 
i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
 */

package airbnb.p336;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class Solution {
  public List<List<Integer>> palindromePairs(String[] words) {
    List<List<Integer>> results = new ArrayList<>();

    if (words == null || words.length < 2) return results;

    HashMap<String, Integer> wordIdxMap = new HashMap<>();
    for(int i = 0; i < words.length; i++) {
      wordIdxMap.put(words[i], i);
    }

    for(int i = 0; i < words.length; i++) {
      // Note: here j <= words[i].length
      for (int j = 0; j <= words[i].length(); j++) {
        // substring(beginIdx, endIdx) returns beginIdx..endIdx-1
        String leftSub = words[i].substring(0, j);
        // substring(beginIdx) if beginIdx == string.length, it will return empty string
        String rightSub = words[i].substring(j);

        if (isPalindrome(leftSub)) {
          addPair(wordIdxMap, results, rightSub, i, true);
        }

        if (rightSub.length() != 0 && isPalindrome(rightSub)) {
          addPair(wordIdxMap, results, leftSub, i, false);
        }
      }
    }

    return results;
  }


  private void addPair(HashMap<String, Integer> wordIdxMap, List<List<Integer>> results, String subToLookUp, int currentIdx, boolean isReverse) {
    String reversedSub = new StringBuilder(subToLookUp).reverse().toString();
    if (wordIdxMap.containsKey(reversedSub) && wordIdxMap.get(reversedSub) != currentIdx) {
      List<Integer> pair = new ArrayList<>();
      
      if (isReverse) {
        pair.add(wordIdxMap.get(reversedSub));
        pair.add(currentIdx);
      } else {
        pair.add(currentIdx);
        pair.add(wordIdxMap.get(reversedSub));
      }

      results.add(pair);
    }
  }

  private boolean isPalindrome(String str) {
    int left = 0;
    int right = str.length() - 1;

    while(left <= right) {
      if (str.charAt(left) != str.charAt(right)) return false;
      left++;
      right--;
    }

    return true;
  }

  public static void main(String[] args) {
    Solution sol = new Solution();
    String[] test1 = { "abcd", "dcba", "lls", "s", "sssll" };
    List<List<Integer>> results = sol.palindromePairs(test1);

    for (List<Integer> pair : results) {
      System.out.format("(%d, %d)\n", pair.get(0), pair.get(1));
    }
  }
}
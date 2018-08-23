/**
https://leetcode.com/problems/alien-dictionary/description/
http://www.cnblogs.com/grandyang/p/5250200.html

1. The key point is to consider topological sorting.
2. When compare two words, the first different char in the two words decides
   the order of them.
 */

package airbnb.p269;

import java.util.*;

public class Solution {
  public String alienOrder(String[] words) {
    if (words == null || words.length == 0) return "";

    Map<Character, Set<Character>> adjacencies = new HashMap<>();
    Map<Character, Integer> indegrees = new HashMap<>();

    for(int i=0; i<words.length; i++) {
      for(char ch : words[i].toCharArray()) {
        indegrees.put(ch, 0);
      }
    }

    // build the graph and indegress
    for(int i=0; i<words.length - 1; i++) {
      String current = words[i];
      String next = words[i+1];

      int length = Math.min(current.length(), next.length());
      for(int j=0; j<length; j++) {
        char currentChar = current.charAt(j);
        char nextChar = next.charAt(j);

        if(currentChar != nextChar) {
          Set<Character> neighborsSet;
          if (adjacencies.containsKey(currentChar)) {
            neighborsSet = adjacencies.get(currentChar);
          } else {
            neighborsSet = new HashSet<Character>();
            adjacencies.put(currentChar, neighborsSet);
          }

          if(!neighborsSet.contains(nextChar)) {
            neighborsSet.add(nextChar);
            indegrees.put(nextChar, indegrees.get(nextChar) + 1);
          }
          break;
        }
      }
    }

    // create a queue with all 0-indegree nodes
    Queue<Character> queue = new LinkedList<>();
    for(Map.Entry<Character, Integer> entry : indegrees.entrySet()) {
      if(entry.getValue() == 0) {
        queue.add(entry.getKey());
      }
    }

    // Use kahn's algorithm to do topological sorting
    StringBuilder answer = new StringBuilder();
    while(!queue.isEmpty()) {
      char ch = queue.remove();
      answer.append(ch);

      if(adjacencies.containsKey(ch)) {
        for(char neighbor : adjacencies.get(ch)) {
          indegrees.put(neighbor, indegrees.get(neighbor) - 1);
          if(indegrees.get(neighbor) == 0) {
            queue.add(neighbor);
          }
        }
      }
    }

    if (answer.length() == indegrees.size()) {
      return answer.toString();
    } else {
      return "";
    }
  }

  public static void main(String[] args) {
    Solution sol = new Solution();
    String[] test1 = {"wrt", "wrf", "er", "ett", "rftt"};
    System.out.println(sol.alienOrder(test1));
  }
}
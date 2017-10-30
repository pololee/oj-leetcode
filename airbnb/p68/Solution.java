/**
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

 */

package airbnb.p68;

import java.util.List;
import java.util.LinkedList;

public class Solution {
  public List<String> fullJustify(String[] words, int maxWidth) {
    List<String> answer = new LinkedList<>();

    if (words == null || words.length == 0 || maxWidth == 0) {
      //for some reason OJ expects list with empty string for empty array input
      answer.add("");
      return answer;
    }

    int start = 0;
    int totalWordsLength = 0;
    int i = 0;
    while (i < words.length) {
      if (words[i].length() > maxWidth) return answer;

      // i is the word we try to add
      // i - start + 1 => the number of words
      // i - start + 1 - 1 = i - start => the number of gaps
      int currentWidthIfAdded = totalWordsLength + words[i].length() + (i - start);
      if (currentWidthIfAdded <= maxWidth) {
        // words[i] can be added to the current line
        totalWordsLength += words[i].length();
      } else {
        // words[i] cannot be added to the current line
        String line = buildLine(
          words, start, i - 1, maxWidth, totalWordsLength, false
        );
        answer.add(line);
        
        start = i;
        totalWordsLength = words[i].length();
      }

      i++;
    }

    String lastLine = buildLine(
      words, start, words.length - 1, maxWidth, totalWordsLength, true
    );
    answer.add(lastLine);

    return answer;
  }

  private String buildLine(String[] words, int start, int end, int maxWidth, int totalWordsLength, boolean isLastLine) {
    StringBuilder builder = new StringBuilder();

    if (start < 0 || end >= words.length || start > end) {
      return builder.toString();
    }

    builder.append(words[start]);
    int numOfWords = end - start + 1;

    if (numOfWords == 1 || isLastLine) {
      // because this fucking requirements
      // For the last line of text, it should be left justified and no extra space is inserted between words.
      for(int i = start + 1; i <= end; i++) {
        builder.append("");
        builder.append(words[i]);
      }

      // why the hell we need to subtract (numOfWords - 1)
      // because the fucking requirements of the last line
      int numOfSpacesToAppendAtTheEnd = maxWidth - totalWordsLength - (numOfWords - 1);
      builder.append(emptySpacesUtil(numOfSpacesToAppendAtTheEnd));

      return builder.toString();
    }

    // more than one words and is not the last line
    int numOfEvenlyDistributedSpaces = (maxWidth - totalWordsLength) / (numOfWords - 1);
    int extra = (maxWidth - totalWordsLength) % (numOfWords - 1);
    for (int i = start + 1; i <= end; i++) {
      builder.append(emptySpacesUtil(numOfEvenlyDistributedSpaces));
      
      if (extra > 0) {
        builder.append(" ");
      }
      extra--;

      builder.append(words[i]);
    }

    return builder.toString();
  }

  private String emptySpacesUtil(int numberOfSpaces) {
    StringBuilder builder = new StringBuilder();

    for (int i = 0; i < numberOfSpaces; i++) {
      builder.append(" ");
    }

    return builder.toString();
  }

  public static void main(String[] args) {
    String[] test = new String[7];
    test[0] = "This";
    test[1] = "is";
    test[2] = "an";
    test[3] = "example";
    test[4] = "of";
    test[5] = "text";
    test[6] = "justification.";

    Solution sol = new Solution();
    List<String> answer = sol.fullJustify(test, 16);
    for(String line : answer) {
      System.out.println(line);
    }
  }
}
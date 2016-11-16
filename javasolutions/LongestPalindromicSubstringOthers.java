public class LongestPalindromicSubstringOthers {
  // O(n^3)
  // n(n - 1) substring
  // check each substring need O(n)
  public String bruteForce(String str) {
    int maxLength = 0;
    String longestSub = "";

    for (int i = 0; i < str.length(); i++) {
      for (int j = i + 1; j < str.length(); j++) {
         int currentLength = j - i + 1;
         String currentSub = str.substring(i, j + 1);
         if (isPalindromic(currentSub)) {
           if (currentLength > maxLength) {
             maxLength = currentLength;
             longestSub = currentSub;
           }
         }
      }
    }

    return longestSub;
  }

  private boolean isPalindromic(String str) {
    for (int i = 0, j = str.length() - 1; i <= j; i++, j--) {
      if (str.charAt(i) != str.charAt(j)) {
        return false;
      }
    }

    return true;
  }

  // VersionOne and VersionTwo are not good implementation
  public String expandFromCenterVersionOne(String str) {
    int startSub = 0, endSub = 0;

    int[] beginAndEndIndicesWithOddLength = new int[2];
    int oddLength = 0;
    int[] beginAndEndIndicesWithEvenLength = new int[2];
    int evenLength = 0;

    int currentStartSub = 0, currentEndSub = 0;

    for (int i = 0; i < str.length(); i++) {
      tryExpandAroundCenterVersionOne(str, i, i, beginAndEndIndicesWithOddLength);
      tryExpandAroundCenterVersionOne(str, i, i + 1, beginAndEndIndicesWithEvenLength);

      oddLength = beginAndEndIndicesWithOddLength[1] - beginAndEndIndicesWithOddLength[0] + 1;
      evenLength = beginAndEndIndicesWithEvenLength[1] - beginAndEndIndicesWithEvenLength[0] + 1;

      if (oddLength > evenLength) {
        currentStartSub = beginAndEndIndicesWithOddLength[0];
        currentEndSub = beginAndEndIndicesWithOddLength[1];
      } else {
        currentStartSub = beginAndEndIndicesWithEvenLength[0];
        currentEndSub = beginAndEndIndicesWithEvenLength[1];
      }

      if (currentEndSub -  currentStartSub > endSub - startSub) {
        startSub = currentStartSub;
        endSub = currentEndSub;
      }
    }

    return str.substring(startSub, endSub + 1);
  }

  private void tryExpandAroundCenterVersionOne(String str, int leftCenter, int rightCenter, int[] beginAndEndIndices) {
    int left = leftCenter, right = rightCenter;
    while (left >= 0 && right < str.length() && str.charAt(left) == str.charAt(right)) {
      left--;
      right++;
    }

    beginAndEndIndices[0] = left + 1;
    beginAndEndIndices[1] = right - 1;
  }

  public String expandFromCenterVersionTwo(String str) {
    int start = 0, end = 0;

    for (int i = 0; i < str.length(); i++) {
      int oddLength = tryExpandAroundCenterVersionTwo(str, i, i);
      int evenLength = tryExpandAroundCenterVersionTwo(str, i, i + 1);

      int maxLen = Math.max(oddLength, evenLength);

      // This is probably the most trick part of this version
      // When maxLen is oddLength,
      //   start = i - (oddLength - 1) / 2, end = i + (oddLength + 1) / 2;
      // When maxLen is evenLength,
      //   start = i - (evenLength - 2) / 2, end = i + (evenLength) / 2
      //
      if (maxLen > (end - start + 1)) {
        start = i - (maxLen - 1) / 2;
        end = i + maxLen / 2;
      }
    }

    return str.substring(start, end + 1);
  }

  private int tryExpandAroundCenterVersionTwo(String str, int leftCenter, int rightCenter) {
    int left = leftCenter, right = rightCenter;
    while (left >= 0 && right < str.length() && str.charAt(left) == str.charAt(right)) {
      left--;
      right++;
    }

    return right - left - 1;
  }

  public static void main(String[] args) {
    LongestPalindromicSubstringOthers finder = new LongestPalindromicSubstringOthers();

    System.out.println(finder.bruteForce("abacdfgdcaba"));
  }
}

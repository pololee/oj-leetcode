package javasolutions.p459;

public class RepeatedSubstringPattern {
  public boolean repeatedSubstringPattern(String str) {
    int length = str.length();

    for(int patternLength=length/2; patternLength>=1; patternLength--) {
      if(length % patternLength == 0) {
        String pattern = str.substring(0, patternLength);

        int numOfPatterns = length / patternLength;
        int j = 1;
        for (; j<numOfPatterns; j++) {
          if(!pattern.equals(str.substring(patternLength * j, patternLength * (j+1)))) break;
        }

        if (j == numOfPatterns) {
          System.out.println(patternLength);
          System.out.println(numOfPatterns);
          return true;
        }
      }
    }

    return false;
  }

  public static void main(String[] args) {
    RepeatedSubstringPattern cal = new RepeatedSubstringPattern();

    System.out.println(cal.repeatedSubstringPattern("aba"));
    System.out.println(cal.repeatedSubstringPattern("abcabcabcabc"));
  }
}
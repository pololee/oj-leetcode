package airbnb.p68;

import java.util.List;
import java.util.LinkedList;

class SolutionSubmitted {
    private String[] words;
    private int maxWidth;
    
    private String emptySpacesUtil(int number) {
      StringBuilder builder = new StringBuilder();
      
      for(int i = 0; i < number; i++) {
          builder.append(" ");
      }
      
      return builder.toString();
    }
    
    private String buildLine(int start, int end, int totalWordsWidth, boolean isLastLine) {
      StringBuilder builder = new StringBuilder();
      
      if (start < 0 || end > words.length || start > end) {
        return builder.toString();
      }
      
      builder.append(words[start]);
      int numberOfWords = end - start + 1;
      
      if (numberOfWords == 1 || isLastLine) {
        for(int i=start + 1; i <= end; i++) {
            builder.append(" ");
            builder.append(words[i]);
        }
        
        int numberOfSpacesToAppend = maxWidth - totalWordsWidth - (numberOfWords - 1);
        builder.append(emptySpacesUtil(numberOfSpacesToAppend));
        
        return builder.toString();
      }

      int space = (maxWidth - totalWordsWidth) / (numberOfWords - 1);
      int extra = (maxWidth - totalWordsWidth) % (numberOfWords - 1);

      for(int i = start + 1; i <= end; i++) {
        builder.append(emptySpacesUtil(space));

        if (extra > 0) {
          builder.append(" ");
          extra--;
        }

        builder.append(words[i]);
      }

      return builder.toString();
    }

    public List<String> fullJustify(String[] words, int maxWidth) {
      List<String> answer = new LinkedList<>();

      if (words == null || words.length == 0 || maxWidth <= 0) {
        answer.add("");
        return answer;
      }

      this.words = words;
      this.maxWidth = maxWidth;

      int start = 0;
      int totalWordsWidth = 0;

      for(int i = 0; i < words.length; i++) {
        if (words[i].length() > this.maxWidth) {
          return answer;
        }

        int currentLineIfAdded = totalWordsWidth + words[i].length() + (i - start);
        if (currentLineIfAdded <= this.maxWidth) {
          totalWordsWidth += words[i].length();
        } else {
          String line = buildLine(start, i - 1, totalWordsWidth, false);
          answer.add(line);

          start = i;
          totalWordsWidth = words[i].length();
        }
      }

      String lastLine = buildLine(start, words.length - 1, totalWordsWidth, true);
      answer.add(lastLine);

      return answer;
    }
}
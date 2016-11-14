/*
Similar to Question [15. Read N Characters Given Read4],
but the read function may be called multiple times.

Need to handle the case, where last time the read was called, there
could be a partial read from buf4, which means some bytes are left in buf4.
Next read call should take the bytes left in buf4 first.

private member variables

buf4: store bytes read from read4
idxNextReadCallStart: offset idx to indicate the position in buf4 where the Next
                      read call should start from
numOfBytesInBuf4: how many bytes are read from read4 stored in buf4 (it could be < 4)
 */

public class ReadNCharsGivenRead4CallMultipleTimes extends Reader4 {
  private char[] buf4 = new char[4];

  private int idxNextReadCallStart = 0, numOfBytesInBuf4 = 0;

  /**
   * [read description]
   * @param   buf Destination buffer
   * @param   n Maximum number of characters to read
   * @return  The actual number of characters that were read
   */
  public int read(char[] buf, int n) {
    int numOfBytesWereCopied = 0;
    boolean eof = false;

    while (!eof && numOfBytesWereRead < n) {
      int numOfBytesIHave = (numOfBytesInBuf4 > 0) ? numOfBytesInBuf4 : read4(buf4);

      // numOfBytesInBuf4 == 0 means numOfBytesIHave is number of bytes that were read
      // from read4.
      // I read4 returns < 4, it means it reaches the end of the file.
      if (numOfBytesInBuf4 == 0 && numOfBytesIHave < 4) {
        eof = true;
      }

      int numOfBytesNeedToCopy = Math.min(n - numOfBytesWereCopied, numOfBytesIHave);
      System.arraycopy(buf4, idxNextReadCallStart, buf, numOfBytesWereCopied, numOfBytesNeedToCopy);

      numOfBytesWereCopied += numOfBytesNeedToCopy;

      idxNextReadCallStart = (idxNextReadCallStart + numOfBytesNeedToCopy) % 4;
      numOfBytesInBuf4 = numOfBytesIHave - numOfBytesNeedToCopy;
    }

    return numOfBytesWereCopied;
  }
}

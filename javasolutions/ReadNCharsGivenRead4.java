/*
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there
is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note: The read function will only be called once for each test case.
 */

// When read4 returns less than 4, we know it must reached the end of file.
// However, take note that read4 returning 4 could mean the last 4 bytes of the file.

public class ReadNCharsGivenRead4 extends Reader4 {
  /**
   * [read description]
   * @param   buf Destination buffer
   * @param   n Maximum number of characters to read
   * @return  The actual number of characters that were read
   */
  public int read(char[] buf, int n) {
    char[] buffer = int char[4];
    int actualCharWereRead = 0;
    boolean eof = false;

    while(!eof && actualCharWereRead < n) {
      int readFromReader4 = read4(buffer);
      if (readFromReader4 < 4) {
        eof = true;
      }

      int numOfBytesToCopy = Math.min(n - actualCharWereRead, readFromReader4);
      System.arraycopy(buffer, 0, buf, actualCharWereRead, numOfBytesToCopy);
      actualCharWereRead += numOfBytesToCopy;
    }

    return actualCharWereRead;
  }
}

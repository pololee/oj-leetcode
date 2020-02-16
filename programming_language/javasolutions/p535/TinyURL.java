/**
 * Good reading: https://segmentfault.com/a/1190000006140476
 *
 * Leetcode link: https://leetcode.com/problems/encode-and-decode-tinyurl/?tab=Description
 */

package javasolutions.p535;

import java.util.HashMap;

public class TinyURL {
  private HashMap<Long, String> dbRecord; // key: auto-increment ID, value: long URL

  private static long COUNTER;
  private static final String ELEMENTS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  private static final String TINY_DOMAIN = "http://tiny.url/";

  public TinyURL() {
    dbRecord = new HashMap<Long, String>();
    COUNTER = 1;
  }

  public String encode(String longUrl) {
    String shortUrl = base10ToBase62(COUNTER);
    dbRecord.put(COUNTER, longUrl);
    COUNTER++;

    return TINY_DOMAIN + shortUrl;
  }

  public String decode(String shortUrl) {
    String base62Str = shortUrl.substring(TINY_DOMAIN.length());
    long id = base62ToBase10(base62Str);

    return dbRecord.get(id);
  }

  private long base62ToBase10(String base62Str) {
    long id = 0;
    for (int i = 0; i < base62Str.length(); i++) {
      id = id * 62 + convert(base62Str.charAt(i));
    }

    return id;
  }

  private int convert(char ch) {
    if (ch >= '0' && ch <= '9') {
      return ch - '0';
    }

    if (ch >= 'a' && ch <= 'z') {
      return ch - 'a' + 10;
    }

    if (ch >= 'A' && ch <= 'Z') {
      return ch - 'A' + 36;
    }

    return -1;
  }

  private String base10ToBase62(long id) {
    StringBuilder builder = new StringBuilder();

    while (id != 0) {
      int index = (int) id % 62;
      builder.insert(0, ELEMENTS.charAt(index));
      id /= 62;
    }

    while (builder.length() != 6) {
      builder.insert(0, '0');
    }

    return builder.toString();
  }

  public static void main(String[] args) {
    TinyURL service = new TinyURL();

    String test = "https://discuss.leetcode.com/topic/81590/a-common-way-using-62-letters-java";
    String shortUrl = service.encode(test);

    System.out.println(shortUrl);
    System.out.println(test);
    System.out.println(service.decode(shortUrl));
  }
}
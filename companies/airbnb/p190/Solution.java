/**
https://leetcode.com/problems/reverse-bits/#/description

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

basically, just pick each bit
 */

package airbnb.p190;

public class Solution {
  // you need treat n as an unsigned value
  public int reverseBits(int n) {
      int answer = 0;
      for(int i = 0; i < 32; i++) {
          if((n & 1) == 1) {
              answer = (answer << 1) + 1;
          } else {
              answer = answer << 1;
          }

          n = n >> 1;
      }

      return answer;
  }
}

# Let's see the relationship between the Excel sheet column title and the number:

# A   1     AA    26 + 1     BA  2×26 + 1     ...     ZA  26×26 + 1     AAA  1×26²+1×26 + 1
# B   2     AB    26 + 2     BB  2×26 + 2     ...     ZB  26×26 + 2     AAB  1×26²+1×26 + 2
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
# Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

# But how to get the column title from the number? We can't simply use the n % 26 method because:

# ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

# We can use(n-1) % 26 instead, then we get a number range from 0 to 25.

import string


class Solution:
    UPPERCASE_LETTERS = list(string.ascii_uppercase)
    BASE = 26

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = []
        while n > 0:
            remainder = (n - 1) % self.BASE
            output.append(self.UPPERCASE_LETTERS[remainder])
            n = (n - 1) // self.BASE
        
        output.reverse()
        return ''.join(output)

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        addOne = 0
        answer = []

        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0

            the_sum = a + b + addOne
            answer.append(str(the_sum % 10))
            addOne = the_sum // 10

            i -= 1
            j -= 1
        if addOne > 0:
            answer.append(str(addOne))
        answer.reverse()
        return ''.join(answer)

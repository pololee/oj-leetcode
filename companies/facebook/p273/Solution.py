class Solution:

    LESS_THAN_TWENTY = ["", "One", "Two", "Three", "Four", "Five",
                        "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                        "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    TEN_TIMES = ["", "", "Twenty", "Thirty", "Fourty", "Fifty",
                 "Sixty", "Seventy", "Eighty", "Ninety"]
    
    UNIT = ["Thousand", "Million", "Billion"]

    def number_to_words(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        answer = self.convert_hundred(num % 1000)
        for i in range(3):
            num //= 1000

            if num % 1000 > 0:
                following = " " + answer if answer else ""
                answer = self.convert_hundred(num % 1000) + " " + self.UNIT[i] + following
        
        return answer

    def convert_hundred(self, num):
        answer = ""

        a = num // 100
        b = num % 100
        c = num % 10

        if b < 20:
            answer = self.LESS_THAN_TWENTY[b]
        else:
            following = " " + self.LESS_THAN_TWENTY[c] if c > 0 else ""
            answer = self.TEN_TIMES[b // 10] + following

        if a > 0:
            following = " " + answer if answer else ""
            answer = self.LESS_THAN_TWENTY[a] + " Hundred" + following

        return answer

def main():
    sol = Solution()
    # print(sol.convert_hundred(123))
    # print(sol.convert_hundred(101))
    # print(sol.convert_hundred(210))
    # print(sol.convert_hundred(200))
    print(sol.number_to_words(123))
    print(sol.number_to_words(12345))
    print(sol.number_to_words(1234567))

if __name__ == "__main__":
    main()

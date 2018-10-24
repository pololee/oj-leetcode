class BasicCalculator:
    def evaluate(self, expression):
        if not expression:
            return 0
        
        ans = 0
        signStack = [1]
        sign = 1

        for i in range(len(expression)):
            ch = expression[i]

            if ch == '(':
                


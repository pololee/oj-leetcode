class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []
        for i in range(len(asteroids)):
            cur_ast = asteroids[i]
            
            if not stack or not self.will_collide(stack[-1], cur_ast):
                stack.append(cur_ast)
                continue
            
            while stack and stack[-1] > 0 and abs(stack[-1]) < abs(cur_ast):
                stack.pop()
            
            # case 1: stack is empty
            # case 2: stack[-1] < 0
            # case 3: abs(stack[-1]) >= abs(cur_ast)
            if not stack or stack[-1] < 0:
                stack.append(cur_ast)
                continue
            
            if abs(stack[-1]) == abs(cur_ast):
                stack.pop()

        return stack

    def will_collide(self, prev_ast, cur_ast):
        if prev_ast > 0 and cur_ast < 0:
            return True

        return False

def main():
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))
    print(sol.asteroidCollision([8, -8]))
    print(sol.asteroidCollision([10, 2, -5]))
    print(sol.asteroidCollision([-2, -1, 1, 2]))
    

if __name__ == '__main__':
    main()

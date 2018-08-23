#            * * * * * * * *
#            * * X * X * * *
#            * X * * * X * *
#            * * * K * * * *
#            * X * * * X * *
#            * * X * X * * *
#            * * * * * * * *
#            * * * * * * * *
# Given start position x, y and N moves, 
# what's the probability that the king remains on board in N moves?

class KingProbability:
    def remainOnBoardProb(self, x, y, N):
        DP = [[0.0 for _ in range(8)] for _ in range(8)]
        DP[x][y] = 1.0

        for i in range(N):
            pass
        
        return 0.0

# class KingProbability:
#     def remainOnBoardProb(self, x, y, N):
#         self.answer = 0

#         return self.answer
    
#     def remain_util(self, x, y, prob, moves):
#         if not self.on_board(x, y):
#             return
        
#         if moves == 0:
#             self.answer += prob
#             return
        
#         for direction in directions:
#             new_x
#             new_y
#             self.remain_util(new_x, new_y, prob * 1/8, moves - 1)

    
#     def on_board(self, x, y)



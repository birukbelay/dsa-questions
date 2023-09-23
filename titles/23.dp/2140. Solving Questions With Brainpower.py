# https://leetcode.com/problems/solving-questions-with-brainpower/
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        L=len(questions)
        dp=[0]*L
        
        for i in range(L-1, -1, -1):
            fut=  i + questions[i][1] +1
            
            if fut < L:
                dp[i] = questions[i][0] + dp[fut]
            else:
                dp[i] = questions[i][0]
            
            if(i < L-1):
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]
                
                
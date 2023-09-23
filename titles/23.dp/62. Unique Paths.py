# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            if row ==m-1 and col ==n-1:
                return 1
            state= (row, col)
            if row>=m:
                memo[state]=0
                return 0

            if col >=n:
                memo[state]=0
                return 0

            
            if state in memo:
                return memo[state]
            right = dp(row, col+1)
            bottom = dp(row+1, col)

            memo[state]= right + bottom

            return right + bottom
        return dp(0,0)




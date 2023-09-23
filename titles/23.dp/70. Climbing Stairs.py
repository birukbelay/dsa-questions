# https://leetcode.com/problems/climbing-stairs/

"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo ={}
        def dp(n):		 
            if n == 1 or n==2:
                return n
            if n in memo:
                return memo[n]
            ans = dp(n - 1) + dp(n - 2)
            memo[n]= ans
            return ans
        return dp(n)
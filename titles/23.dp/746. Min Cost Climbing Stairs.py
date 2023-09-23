# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.append(0)
        # for i in range(len(cost)-3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])
        
        N= len(cost)
        memo = {}
        def dp(i):
            if i==N-1:
                return cost[i]
            if i ==N-2:
                return min(cost[N-1] + cost[i], cost[i])
            if i in memo:
                return memo[i]
            
            jump = cost[i] +dp(i+1)
            
            step = cost[i] + dp(i+2)
            
            result = min(step, jump)
            memo[i] = result
            return result
        return min(dp(0), dp(1))
        
        
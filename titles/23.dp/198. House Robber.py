# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        memo = {}
        def dp(i, N):
            if i==N-1:
                return nums[i]
            if i ==N-2:
                return max(nums[N-1], nums[i])
            if i in memo:
                return memo[i]
            
            no_rob = dp(i+1)
            
            rob = nums[i] + dp(i+2)
            
            result = max(rob, no_rob)
            memo[i] = result
            return result
        N= len(nums)
        first = dp(0, N-1)
        second = dp(1, N)

        return max(first, second)
        
        
        
        
        rob1, rob2 = 0,0        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2    
            
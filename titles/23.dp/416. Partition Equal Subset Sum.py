class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dp(i, half_sum):
            if i>=n or half_sum == 0:
                return half_sum == 0
            if half_sum<0:
                return False
            state = (i, half_sum)
            if state in memo:
                return memo[state]

            subtract = dp(i+1, half_sum- nums[i])
            if subtract == True:
                memo[state]= True
                return True
            no_subtract = dp(i+1, half_sum)
            result = subtract or no_subtract
            memo[state]= result
            return result

        
        sums = sum(nums)
        if sums%2 !=0:
            return False
        return dp(0, sums//2)
        
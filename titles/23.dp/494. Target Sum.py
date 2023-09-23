class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo ={}
        def dp(i, tot):
            if i>=len(nums):
                return 1 if tot==target else 0
            state = (i, tot)
            if state in memo:
                return memo[state]
            add = dp(i+1, tot+ nums[i])

            subtract = dp(i+1, tot -nums[i])
            memo[state]= add + subtract
            return add + subtract
        return dp(0,0)
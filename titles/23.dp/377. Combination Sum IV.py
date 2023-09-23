class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # top down
        dp = [-1] * (target+1)
        dp[0] =1
        def helper(numbers, tar):
            if dp[tar] !=-1:
                return dp[tar]
            res=0
            for i in range(len(numbers)):
                if tar >= numbers[i]:
                    res += helper(numbers, tar - numbers[i])
            dp[tar] = res
            return res
        
        
        return helper(nums, target)
        
        
        # --------------  Bottom Up


        # comb = [0] * (target +1)
        # comb[0]=1
        # for i in range(1,len(nums)):
        #     for j in range(len(nums)):
        #         if i-nums[j] >=0:
        #             comb[i] += comb[i- nums[j]]
        # return comb[target]
        
        dp = {0:1}
        for total in range(1, target +1):
            dp[total]=0
            for n in nums:
                dp[total] += dp.get(total-n, 0)
        
        return dp[target]
        
        
        # memo ={}
        # result =[]
        # cur =[]
        # def dp(i):
        #     tot = sum(cur)
        #     if i>= len(nums) or sum(cur)> target:               
        #         return 0
        #     state = (target-nums[i])
        #     if tot ==target:
        #         memo[state]= memo.get(state, 1)
        #         # result.append(cur[:])
        #         return memo[state]
            
        #     if state in memo:
        #         return memo[state]

        #     ans=0
        #     # a decision where we include the candidate
        #     cur.append(nums[i])        
        #     ans += dp(i)
        #     # a decision where we include the candidate
        #     cur.pop()
        #     ans += dp(i+1)
        #     return ans
        # return dp(0)
        # return result




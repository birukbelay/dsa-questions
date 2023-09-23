# https://leetcode.com/problems/reducing-dishes/description/
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        memo={}
        def dp(idx, time):


            if idx==len(satisfaction):
                return 0

            state =(idx, time)
            if state in memo:
                return memo[state]           
            # 1. Cook the dish at `index` with the time taken as `time` and move on to the next dish with time as time + 1.
            
            
            cur = satisfaction[idx] * time
            pick = dp(idx +1, time +1)

            # 2. Skip the current dish and move on to the next dish at the same time.
            notPick = dp(idx +1, time)

            

            # Return the maximum of two choices:            
            memo[state]=max(notPick , pick + cur)
            return memo[state]
        return dp(0, 1)


        # Greedy way
        suffixSum = satisfaction[:]
        for i in range(len(satisfaction)-2, -1, -1):
            suffixSum[i] += suffixSum[i+1]

        tot=0

        for i in range(len(satisfaction)-1, -1, -1):
            cur = suffixSum[i]
            if cur<0:
                break
            tot +=cur
        return tot
        

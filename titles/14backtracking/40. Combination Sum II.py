# https://leetcode.com/problems/combination-sum-ii/
# unique conbinations, each no can only be used once
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        cur =[]
        candidates.sort()
        def soln(i):
            if sum(cur)==target:
                result.append(cur[:])
                return
            if i>= len(candidates) or sum(cur)> target:               
                return      
            # a decision where we include the candidate
            cur.append(candidates[i])        
            soln(i+1)
            # a decision where we include the candidate
            cur.pop()
            # not to include the same candidate twice
            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            soln(i+1)
        soln(0)
        return result
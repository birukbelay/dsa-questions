# https://leetcode.com/problems/combination-sum/
# Returning list of unique combinations, each no can be used unlimited times
from typing  import List

# class Solution:
def combinationSum1(candidates: List[int], target: int) -> List[List[int]]:
    result =[]
    cur =[]
    def soln(i):
        if sum(cur)==target:
            result.append(cur[:])
            return
        if i>= len(candidates) or sum(cur)> target:               
            return      
        # a decision where we include the candidate
        cur.append(candidates[i])        
        soln(i)
        # a decision where we include the candidate
        cur.pop()
        soln(i+1)
    soln(0)
    return result

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:

    res =[]        
    
    def dfs(i, cur, tot):
        if tot== target: 
            res.append(cur.copy())
            return
        if i> len(candidates) or tot> target:
            return
        # a decision where we include the candidate
        cur.append(candidates[i])
        dfs(i, cur, tot+candidates[i])

        cur.pop()
        dfs(i+1, cur, tot)
    dfs(0, [], 0)
    return res


print(combinationSum1([2,3,6,7], 7))
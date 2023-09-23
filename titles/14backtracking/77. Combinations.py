# https://leetcode.com/problems/combinations/

# time complexity is k.n^k


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allComb = []
    
        def backtrack(start, comb):
            if len(comb)==k:
                allComb.append(comb[:])
                return
            for i in range(start, n+1):
                # decision to add a number into the combination
                comb.append(i)                           
                backtrack(i+1, comb)
                # decide to remove a num from the combination     
                comb.pop()
        backtrack(1, [])
        return allComb
            
            


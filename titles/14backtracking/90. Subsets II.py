# https://leetcode.com/problems/subsets-ii/



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        subset=[]
        def dfs(i):
            if i== len(nums):
                result.append(subset[:])
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+ 1)
            
            # decision not to include nums[i]
            subset.pop()
            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return result
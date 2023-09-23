# Easy
# https://leetcode.com/problems/contains-duplicate-ii/submissions/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dc={}
        for i in range(len(nums)):            
            r=nums[i]                   
            if r in dc:                
                if i-dc[r]<=k:
                    return True
                else:
                    dc[r]=i
            else:
                dc[r]=i
        return False
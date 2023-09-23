#  https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        totSum=0
        minL=sys.maxsize
        r=0
        for i in range(len(nums)):
            totSum+=nums[i]
            
            while totSum>=target and i>=r:
                minL=min((i-r), minL)
                totSum-=nums[r]
                r+=1
        
        if minL==sys.maxsize:
            return 0
        return minL +1
            
            
        
def findLeft(nums: list[int], target: int) -> int:    
    left=0
    right=len(nums)- 1
    best=None
    while left<= right:
        middle= (left+right)//2
        
        if nums[middle]==target:          
            if middle==0:
                return middle
            right=middle-1
            if nums[middle-1]!=target:
                return middle
        elif nums[middle]> target:
            right = middle-1
        else:
            left=middle+1
    
    
    return -1

def findRight(nums: list[int], target: int) -> int:    
    left=0
    right=len(nums)- 1
    best=0
    while left<= right:
        middle= (left+right)//2
        if nums[middle]==target:
            best= middle
            left=middle+1
            if middle+1>=len(nums):
                return middle
            if nums[middle+1] !=target:
                return middle
        elif nums[middle]> target:
            right = middle-1
        else:
            left=middle+1
    if best==target:
        return best
    return -1

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums)==1 and nums[0]==target:
            return [0, 0]
        left= findLeft(nums, target)
        if left==-1:
            return [-1,-1]
        
        right= findRight(nums, target)
        return [left, right]
    
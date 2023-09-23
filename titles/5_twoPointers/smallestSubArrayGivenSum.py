import sys

# finding smallest sub array that sums to a target
def smallestSubArray(nums, target):
    minWindowsize=sys.maxsize
    start=0
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        while(sum>=target):
            minWindowsize=min(minWindowsize, i-start+1)
            sum-=nums[start]
            start+=1
    return minWindowsize

            
        
    
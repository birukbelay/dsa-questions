
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/
def maxFrequency(nums, k):
    nums.sort()
    numLen=len(nums)
    l,r=0,0
    totalSum=nums[0]
    maxLen=0
    print("nums==",nums)
    while l<=r and r<numLen:
        # this is the length 
        winLength=r-l+1
        # print(f'l-{l},{nums[l]} -- r{r},{nums[r]} --winL={winLength}-- totS={totalSum}')
        # if windows tot sum is greater than sum of nums + k
        if(nums[r]*winLength > totalSum+k ):
            totalSum-=nums[l]
            l+=1            
        else:
            # Updating the valid window length 
            maxLen=max(maxLen, winLength)                      
            
            if(r<numLen):
                r+=1
            if(r<numLen):
                totalSum+=nums[r]
            
    return maxLen
            
print(maxFrequency([1,2,4], 5))         

    
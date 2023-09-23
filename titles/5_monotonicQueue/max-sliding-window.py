#TODO hard 
import collections

# given an array and a window size, give all the biggest elements
# in that window from start of the array to the end
def maxSlidingWindow(nums, k):
    output=[]
    q=collections.deque() #holds the indexes
    l=r=0
    
    while r<len(nums):
        
        # pop smaller numbers from q
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)
        
        # if the left index is greater than the queues first index
        # keeps the window in the given range
        if l>q[0]:
            q.popleft()
            
        # if the right index is greater than the window//
        # which is always once it reaches the window size-> 
        # helps to get to the window size before appending to the oupput
        if (r+1) >=k:
            output.append(nums[q[0]])
            l+=1
        r+=1
    return output
nums = [8,2,4,7]
for right,num in enumerate(nums):
    print(right, num)
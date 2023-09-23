# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
import sys
from collections import deque
 

# Using queue
def shortestSubarray( nums: list[int], k: int) -> int:
    # Initializing a queue
    q = deque()
    
    # creating a prifix sum
    prifix_sum=[0]    
    for i in nums:
        prifix_sum.append(prifix_sum[-1]+i)
    # gap holds the biggest lenth
    gap=sys.maxsize
    for i in range(len(prifix_sum)):
        # minimize the gap by checking it with the initial of the queue 
        # and removing from the queue while it is greater than k
        while q and prifix_sum[i] - prifix_sum[q[0]]>= k:

            gap=min(gap,i-q[0])            
            q.popleft()
        # checking for negative numbers 
        while q and prifix_sum[i]< prifix_sum[q[-1]]:
            q.pop()
        q.append(i)
    
    return gap if gap < sys.maxsize else -1
            
            
            
        
        
        








#  using while Loop //#TODO not done
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:        
        left=0
        right=0
        sum=0
        curCtr=0
        smallestCtr=sys.maxsize        
        while left< len(nums):
            sum+=nums[right]
            curCtr+=1
            if right<len(nums)-1:
                right+=1
            elif right==len(nums)-1 and left<len(nums)-1:
                left+=1
                right= left
                
            if sum>=k:
                print(f'sum={sum}, right={right} smlst={smallestCtr}')
                left+=1
                right=left
                sum=0
                if curCtr<smallestCtr:
                    smallestCtr=curCtr
                curCtr=0
        print("smalestCtr=", smallestCtr)
        if smallestCtr==sys.maxsize:
            return -1
        else:
            return smallestCtr
                         
sub=Solution()
# sub.shortestSubarray([84,-37,32,40,95], 167)


# using For loop, TLE ERROR
def shortestSubarray1( nums: list[int], k: int) -> int:    
    sum=0
    curCtr=0
    smallestCtr=sys.maxsize 
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum+=nums[j]
            curCtr+=1
            if sum>=k:
                # print(f'breaking i={i}, j={j} v={nums[j]}')
                # print(f' sum={sum}, cur={smallestCtr}')
                
                
                if curCtr<smallestCtr:
                    smallestCtr=curCtr
                sum=0
                curCtr=0
                break
        sum=0
        curCtr=0
    if smallestCtr==sys.maxsize:
        return -1
    else:
        return smallestCtr
# shortestSubarray1([84,-37,32,40,95], 167)               
                
           
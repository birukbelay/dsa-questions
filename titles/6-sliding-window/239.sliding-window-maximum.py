# https://leetcode.com/problems/sliding-window-maximum/

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        arr=[]
        l=0
        harr=[]
        d={}
        for i in range(len(nums)):
            heapq.heappush(harr, (-nums[i], i))
            if i-l>= k-1: 
                # print("harr=",harr)
                # print(d)
                while harr[0][1] in d:
                    heapq.heappop(harr)
                num=harr[0][0]
                # print(num)
                arr.append(-num)
                d[l]=nums[l]
                l+=1
                
        return arr
            
                
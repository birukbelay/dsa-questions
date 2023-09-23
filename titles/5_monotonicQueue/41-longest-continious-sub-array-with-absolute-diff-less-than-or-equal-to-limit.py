
import collections



class Solution:
    def longestSubarray1(self, nums: List[int], limit: int) -> int:
        winSize=0
#         decreasing queue
        maxQ=collections.deque()
#     increasing queue
        minQ=collections.deque()
        
        left=0            
        for i in range(len(nums)):
            
            #when new elements comes it kicks all lesser elements
            #so max is always at first
            while maxQ and nums[maxQ[-1]]< nums[i]:
                maxQ.pop()
            maxQ.append(i)
            
            # kicks all greater elements
            while minQ and nums[minQ[-1]] >nums[i]:
                minQ.pop()
            minQ.append(i)
            
            
            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                if nums[maxQ[0]]==nums[left]:
                    maxQ.popleft()
                if nums[minQ[0]]==nums[left]:
                    minQ.popleft()
                left+=1
                
            winSize=max(winSize, i-left +1)
        return winSize
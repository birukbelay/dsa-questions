# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        dicn={}
        arr=[]
        
        count=0
        # creating a dictionary with the elements as key & their frequency as a value
        for i in range(len(nums)):
            if nums[i] in dicn:
                dicn[nums[i]]=dicn[nums[i]]+1
            else:
                dicn[nums[i]]=1
                
        tupleArr=[]
        for key, value in dicn.items():
            heapq.heappush(tupleArr, (value, key))
        print(tupleArr)
        for i in range(len(tupleArr)-k):
            heapq.heappop(tupleArr)
        for i,j in tupleArr:
            print(i, j)
            arr.append(j)
        return arr
            
        print(tupleArr)
        
        
soln=Solution()
soln.topKFrequent([1,1,1,2,2,3],2)
# https://leetcode.com/problems/ugly-number-ii/submissions/
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        ctr=1
        number=1
        ugluNums=[2, 3, 5]
        
        while ctr<n:
            
            newRoot=heapq.heappop(ugluNums)
            
            if newRoot > number:
                ctr+=1
                number=newRoot
                heapq.heappush(ugluNums, 2* newRoot)
                heapq.heappush(ugluNums, 3* newRoot)
                heapq.heappush(ugluNums, 5* newRoot)
        return number
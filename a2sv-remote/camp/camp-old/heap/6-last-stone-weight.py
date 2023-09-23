# https://leetcode.com/problems/last-stone-weight/submissions/


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapArr=[]
        for i in stones:
            heapq.heappush(heapArr, -i)
        while len(heapArr)>1:
            big1= heapq.heappop(heapArr)        
            big2= heapq.heappop(heapArr)
            heapq.heappush(heapArr,big1-big2)
        return -heapArr[0]
# https://leetcode.com/problems/furthest-building-you-can-reach/submissions/
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        ladderHeap=[]
        sum=0
        dcArray=[]
        ctr=0
        lenHeights=len(heights)
        for i in range(lenHeights-1):
            a=heights[i+1] - heights[i]
            if a<0: a=0
            dcArray.append(a)
            
        if ladders>=lenHeights-1:
            return lenHeights-1
        print("dcArr=>",dcArray)
        for i in dcArray:
            if i==0:
                ctr+=1
            elif len(ladderHeap)<ladders:
                heapq.heappush(ladderHeap, i)
                ctr+=1
            else:
                heapq.heappush(ladderHeap, i)
                sum+= heapq.heappop(ladderHeap)
                if sum>bricks:
                    return ctr
                ctr+=1
        return ctr
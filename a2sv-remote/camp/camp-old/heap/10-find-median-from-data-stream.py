# https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:

    leftHeap=[]
    rightHeap=[]
    
    def __init__(self):
        self.arr=[]
        self.leftHeap=[]
        self.rightHeap=[]
        

    def addNum(self, num: int) -> None:
        lleft=len(self.leftHeap)
        lright=len(self.rightHeap)
        if lright ==0:
            heapq.heappush(self.rightHeap, num)
            return
        if  lright > lleft:
            if num > self.rightHeap[0]:
                heapq.heappush(self.rightHeap, num)
                a=heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap, -a)
            else:
                heapq.heappush(self.leftHeap, -num)
        else:
            if lright ==0:
                heapq.heappush(self.rightHeap, num)
                return
            if num < self.rightHeap[0]:
                heapq.heappush(self.leftHeap, -num)
                a=heapq.heappop(self.leftHeap)
                heapq.heappush(self.rightHeap, -a)
            else:
                heapq.heappush(self.rightHeap, num)
                
                
                
                
                
            

    def findMedian(self) -> float:
        lleft=len(self.leftHeap)
        lright=len(self.rightHeap)
        
        if lleft==lright:
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        elif lleft>lright:
            return -self.leftHeap[0]
        else:
            return self.rightHeap[0]
        
        
    
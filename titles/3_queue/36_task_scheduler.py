import heapq
from collections import deque

def leastInterval(self, tasks: List[str], n: int) -> int:
    dict={}
    for task in tasks:        
        if task in dict:
            dict[task]=dict[task]+1
        else:
           dict[task]=1
    
    maxHeap=[-cnt for cnt in dict.values()]
    heapq.heapify(maxHeap)
    time=0
    q=deque()
    while maxHeap or q:
        time +=1
        if maxHeap:
            cnt=1+heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1]==time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

def leastIntervalDict(self, tasks: List[str], n: int) -> int:
    dicn={}
    # lenDict=0
    for task in tasks:        
        if task in dicn:
            dicn[task]=dicn[task]+1
        else:
            lenDict+=1
            dicn[task]=1
    sortedDict=dict(sorted(dicn.items(), key=lambda item: item[1], reverse=True))
    # maxHeap=[-cnt for cnt in dict.values()]
    # heapq.heapify(maxHeap)
    time=0
    q=deque()
    i=0    
    while sortedDict or q:
        time +=1
        lenDict=len(dicn)
        if sortedDict:
            cnt=1+heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
    return time



                
        
            